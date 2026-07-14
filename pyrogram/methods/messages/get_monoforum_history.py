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

from datetime import datetime
from typing import Union, Optional, AsyncGenerator

import pyrogram
from pyrogram import types, raw, utils


async def get_chunk(
    *,
    client: "pyrogram.Client",
    channel_id: Union[int, str],
    peer_id: Union[int, str],
    limit: int = 0,
    offset: int = 0,
    min_id: int = 0,
    max_id: int = 0,
    from_message_id: int = 0,
    from_date: datetime = utils.zero_datetime()
):
    messages = await client.invoke(
        raw.functions.messages.GetSavedHistory(
            parent_peer=await client.resolve_peer(channel_id),
            peer=await client.resolve_peer(peer_id),
            offset_id=from_message_id,
            offset_date=utils.datetime_to_timestamp(from_date),
            add_offset=offset,
            limit=limit,
            max_id=max_id,
            min_id=min_id,
            hash=0
        ),
        sleep_threshold=60
    )

    return await utils.parse_messages(client, messages, replies=0)


class GetMonoforumHistory:
    async def get_monoforum_history(
        self: "pyrogram.Client",
        channel_id: Union[int, str],
        peer_id: Union[int, str],
        limit: int = 0,
        offset: int = 0,
        offset_id: int = 0,
        min_id: int = 0,
        max_id: int = 0,
        offset_date: datetime = utils.zero_datetime()
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Get the direct-message history between a monoforum channel and a specific sender.

        Monoforum channels (Direct Messages) route each sender's messages into a separate
        sublist, addressed by the sender's peer id.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            channel_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the monoforum channel.

            peer_id (``int`` | ``str``):
                Unique identifier of the sender whose sublist to read.

            limit (``int``, *optional*):
                Limits the number of messages to be retrieved.
                By default, no limit is applied and all messages are returned.

            offset (``int``, *optional*):
                Sequential number of the first message to be returned.

            offset_id (``int``, *optional*):
                Identifier of the first message to be returned.

            offset_date (:py:obj:`~datetime.datetime`, *optional*):
                Pass a date as offset to retrieve only older messages starting from that date.

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.

        Example:
            .. code-block:: python

                async for message in app.get_monoforum_history(channel_id, peer_id):
                    print(message.text)
        """
        current = 0
        total = limit or (1 << 31) - 1
        limit = min(100, total)

        while True:
            messages = await get_chunk(
                client=self,
                channel_id=channel_id,
                peer_id=peer_id,
                limit=limit,
                offset=offset,
                from_message_id=offset_id,
                min_id=min_id,
                max_id=max_id,
                from_date=offset_date
            )

            if not messages:
                return

            offset_id = messages[-1].id

            for message in messages:
                yield message

                current += 1

                if current >= total:
                    return
