#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
import functools
import inspect
import io
import logging
import math
import os
from hashlib import md5
from pathlib import PurePath
from typing import Union, BinaryIO, Callable

import pyrogram
from pyrogram import StopTransmission
from pyrogram import raw
from pyrogram.session import Session

log = logging.getLogger(__name__)


class SaveFile:
    async def save_file(
        self: "pyrogram.Client",
        path: Union[str, BinaryIO],
        file_id: int = None,
        file_part: int = 0,
        progress: Callable = None,
        progress_args: tuple = (),
        use_experimental_upload_boost: bool = None
    ):
        """Upload a file onto Telegram servers, without actually sending the message to anyone.
        Useful whenever an InputFile type is required.

        .. note::

            This is a utility method intended to be used **only** when working with raw
            :obj:`functions <pyrogram.api.functions>` (i.e: a Telegram API method you wish to use which is not
            available yet in the Client class as an easy-to-use method).

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            path (``str`` | ``BinaryIO``):
                The path of the file you want to upload that exists on your local machine or a binary file-like object
                with its attribute ".name" set for in-memory uploads.

            file_id (``int``, *optional*):
                In case a file part expired, pass the file_id and the file_part to retry uploading that specific chunk.

            file_part (``int``, *optional*):
                In case a file part expired, pass the file_id and the file_part to retry uploading that specific chunk.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

            use_experimental_upload_boost (``bool``, *optional*):
                If True, refills requests as parts complete, with up to four 512 KiB parts
                in flight, including for small files. If False, uses bounded batches of
                four parts for files larger than 10 MiB and one part otherwise.
                Defaults to the client setting.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            ``InputFile``: On success, the uploaded file is returned in form of an InputFile object.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        async with self.save_file_semaphore:
            if path is None:
                return None

            if use_experimental_upload_boost is None:
                use_experimental_upload_boost = getattr(self, "use_experimental_upload_boost", False)

            part_size = 512 * 1024

            if isinstance(path, (str, PurePath)):
                fp = open(path, "rb")
            elif isinstance(path, io.IOBase):
                fp = path
            else:
                raise ValueError("Invalid file. Expected a file path as string or a binary (not text) file pointer")

            file_name = getattr(fp, "name", "file.jpg")

            fp.seek(0, os.SEEK_END)
            file_size = fp.tell()
            fp.seek(0)

            if file_size == 0:
                raise ValueError("File size equals to 0 B")

            file_size_limit_mib = 4000 if self.me and self.me.is_premium else 2000

            if file_size > file_size_limit_mib * 1024 * 1024:
                raise ValueError(f"Can't upload files bigger than {file_size_limit_mib} MiB")

            file_total_parts = int(math.ceil(file_size / part_size))
            is_big = file_size > 10 * 1024 * 1024
            workers_count = 4 if is_big or use_experimental_upload_boost else 1
            is_missing_part = file_id is not None
            file_id = file_id or self.rnd_id()
            md5_sum = md5() if not is_big and not is_missing_part else None
            session = Session(
                self, await self.storage.dc_id(), await self.storage.auth_key(),
                await self.storage.test_mode(), is_media=True
            )

            try:
                await session.start()

                fp.seek(part_size * file_part)

                async def send_part(rpc):
                    if not await session.invoke(rpc):
                        raise RuntimeError("Telegram rejected an uploaded file part")
                    return len(rpc.bytes)

                tasks = set()
                sent = file_part * part_size
                try:
                    while file_part < file_total_parts or tasks:
                        if use_experimental_upload_boost or not tasks:
                            while file_part < file_total_parts and len(tasks) < workers_count:
                                chunk = fp.read(part_size)
                                expected = min(part_size, file_size - file_part * part_size)
                                if len(chunk) != expected:
                                    raise ValueError("File changed during upload")

                                if md5_sum is not None:
                                    md5_sum.update(chunk)
                                if is_big:
                                    rpc = raw.functions.upload.SaveBigFilePart(
                                        file_id=file_id,
                                        file_part=file_part,
                                        file_total_parts=file_total_parts,
                                        bytes=chunk
                                    )
                                else:
                                    rpc = raw.functions.upload.SaveFilePart(
                                        file_id=file_id,
                                        file_part=file_part,
                                        bytes=chunk
                                    )
                                tasks.add(asyncio.create_task(send_part(rpc)))
                                del chunk, rpc
                                file_part += 1
                                if is_missing_part:
                                    break

                        done, _ = await asyncio.wait(
                            tasks,
                            return_when=asyncio.FIRST_COMPLETED
                        )
                        for task in done:
                            sent += task.result()
                            tasks.remove(task)

                        if is_missing_part:
                            return

                        if progress and (use_experimental_upload_boost or not tasks):
                            func = functools.partial(progress, sent, file_size, *progress_args)
                            if inspect.iscoroutinefunction(progress):
                                await func()
                            else:
                                await self.loop.run_in_executor(self.executor, func)
                finally:
                    for task in tasks:
                        if not task.done():
                            task.cancel()
                    await asyncio.gather(*tasks, return_exceptions=True)

                if md5_sum is not None:
                    md5_sum = md5_sum.hexdigest()

            except StopTransmission:
                raise
            except Exception as e:
                log.exception(e)
                raise
            else:
                if is_big:
                    return raw.types.InputFileBig(
                        id=file_id,
                        parts=file_total_parts,
                        name=file_name,
                    )
                else:
                    return raw.types.InputFile(
                        id=file_id,
                        parts=file_total_parts,
                        name=file_name,
                        md5_checksum=md5_sum
                    )
            finally:
                try:
                    await session.stop()
                finally:
                    if isinstance(path, (str, PurePath)):
                        fp.close()
