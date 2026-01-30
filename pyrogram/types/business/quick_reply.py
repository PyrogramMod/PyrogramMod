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

from typing import List, Optional

import pyrogram
from pyrogram import raw, types
from ..object import Object


class QuickReply(Object):
    """Represents a quick reply shortcut.

    Parameters:
        shortcut_id (``int``):
            Unique identifier of the shortcut.

        shortcut (``str``):
            The shortcut name/trigger.

        top_message (``int``):
            ID of the top message in the shortcut.

        count (``int``):
            Total number of messages in the shortcut.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        shortcut_id: int,
        shortcut: str,
        top_message: int,
        count: int
    ):
        super().__init__(client)

        self.shortcut_id = shortcut_id
        self.shortcut = shortcut
        self.top_message = top_message
        self.count = count

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        quick_reply: "raw.types.QuickReply"
    ) -> "QuickReply":
        return QuickReply(
            client=client,
            shortcut_id=quick_reply.shortcut_id,
            shortcut=quick_reply.shortcut,
            top_message=quick_reply.top_message,
            count=quick_reply.count
        )

    async def get_messages(self) -> List["types.Message"]:
        """Bound method *get_messages* of :obj:`~pyrogram.types.QuickReply`.

        Use as a shortcut for:
            .. code-block:: python

                await quick_reply.get_messages()

        Returns:
            List of :obj:`~pyrogram.types.Message`: On success, a list of messages is returned.
        """
        return await self._client.get_quick_reply_messages(shortcut_id=self.shortcut_id)

    async def send_messages(self, chat_id: Union[int, str]) -> "types.Updates":
        """Bound method *send_messages* of :obj:`~pyrogram.types.QuickReply`.

        Use as a shortcut for:
            .. code-block:: python

                await quick_reply.send_messages(chat_id)

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            :obj:`~pyrogram.types.Updates`: On success, the updates object is returned.
        """
        messages = await self.get_messages()
        return await self._client.send_quick_reply_messages(
            chat_id=chat_id,
            shortcut_id=self.shortcut_id,
            message_ids=[m.id for m in messages]
        )

    async def edit(self, shortcut: str) -> bool:
        """Bound method *edit* of :obj:`~pyrogram.types.QuickReply`.

        Use as a shortcut for:
            .. code-block:: python

                await quick_reply.edit("new_shortcut")

        Parameters:
            shortcut (``str``):
                The new name for the shortcut.

        Returns:
            ``bool``: True on success.
        """
        return await self._client.edit_quick_reply_shortcut(
            shortcut_id=self.shortcut_id,
            shortcut=shortcut
        )

    async def delete(self) -> bool:
        """Bound method *delete* of :obj:`~pyrogram.types.QuickReply`.

        Use as a shortcut for:
            .. code-block:: python

                await quick_reply.delete()

        Returns:
            ``bool``: True on success.
        """
        return await self._client.delete_quick_reply_shortcut(shortcut_id=self.shortcut_id)

    @staticmethod
    def _parse_list(
        client: "pyrogram.Client",
        quick_replies: List["raw.types.QuickReply"]
    ) -> Optional[List["QuickReply"]]:
        if not quick_replies:
            return None

        return types.List([
            QuickReply._parse(client, qr)
            for qr in quick_replies
        ])
