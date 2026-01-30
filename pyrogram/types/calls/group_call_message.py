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

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class GroupCallMessage(Object):
    """A message in a group call.

    Parameters:
        id (``int``):
            Message identifier.

        from_id (:obj:`~pyrogram.types.Chat` | :obj:`~pyrogram.types.User`):
            Sender of the message.

        date (``datetime``):
            Date the message was sent.

        text (``str``):
            Message text.

        is_from_admin (``bool``, *optional*):
            True, if the message was sent by an admin.

        paid_message_stars (``int``, *optional*):
            Price of the message in Telegram Stars.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        from_id: "types.Chat" = None,
        date: datetime,
        text: str,
        is_from_admin: bool = None,
        paid_message_stars: int = None
    ):
        super().__init__(client)

        self.id = id
        self.from_id = from_id
        self.date = date
        self.text = text
        self.is_from_admin = is_from_admin
        self.paid_message_stars = paid_message_stars

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        message: "raw.types.GroupCallMessage",
        users: dict = None,
        chats: dict = None
    ) -> "GroupCallMessage":
        if not message:
            return None

        return GroupCallMessage(
            client=client,
            id=message.id,
            from_id=types.Chat._parse(client, message.from_id, users, chats),
            date=utils.timestamp_to_datetime(message.date),
            text=message.message.text if hasattr(message.message, "text") else message.message,
            is_from_admin=getattr(message, "from_admin", None),
            paid_message_stars=getattr(message, "paid_message_stars", None)
        )
