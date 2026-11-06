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

from typing import Union, BinaryIO, List

import pyrogram
from pyrogram import raw, types


class TranscribeAudio:
    async def transcribe_audio(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int
    ) -> "types.TranscribedAudio":
        """Transcribe a voice or audio message.

        If the result is pending, the final text arrives as :obj:`~pyrogram.types.TranscriptionUpdate`.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the voice or audio message.

        Returns:
            :obj:`~pyrogram.types.TranscribedAudio`: The transcription.

        Example:
            .. code-block:: python

                t = await app.transcribe_audio(chat_id, message_id)
        """
        r = await self.invoke(
            raw.functions.messages.TranscribeAudio(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id
            )
        )

        return types.TranscribedAudio._parse(self, r)

    async def transcribe_audio_file(
        self: "pyrogram.Client",
        audio: Union[str, BinaryIO]
    ) -> "types.TranscribedAudio":
        """Transcribe an audio file that is not in a message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            audio (``str`` | ``BinaryIO``):
                Path or file object of the audio to upload and transcribe.

        Returns:
            :obj:`~pyrogram.types.TranscribedAudio`: The transcription.
        """
        r = await self.invoke(
            raw.functions.messages.TranscribeAudioFile(file=await self.save_file(audio))
        )

        return types.TranscribedAudio._parse(self, r)

    async def get_transcription_langs(
        self: "pyrogram.Client",
        chat_id: Union[int, str] = None
    ) -> List[str]:
        """Get the language codes available for transcription.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``, *optional*):
                Chat the transcription is for.

        Returns:
            List of ``str``: Language codes.
        """
        return await self.invoke(
            raw.functions.messages.GetTranscriptionLangs(
                peer=await self.resolve_peer(chat_id) if chat_id is not None else None
            )
        )
