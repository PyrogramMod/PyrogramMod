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
from typing import Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class BusinessConnection(Object):
    """Represents a business bot connection.

    Parameters:
        id (``str``):
            Unique identifier of the connection.

        user (:obj:`~pyrogram.types.User`):
            The business account user.

        dc_id (``int``):
            Data center ID of the user.

        date (:py:obj:`~datetime.datetime`):
            When the connection was established.

        can_reply (``bool``, *optional*):
            Whether the bot can reply to messages.

        disabled (``bool``, *optional*):
            Whether the connection is disabled.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        user: "types.User" = None,
        dc_id: int = None,
        date: datetime = None,
        can_reply: bool = None,
        disabled: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.user = user
        self.dc_id = dc_id
        self.date = date
        self.can_reply = can_reply
        self.disabled = disabled

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        connection: "raw.types.BotBusinessConnection",
        users: dict
    ) -> "BusinessConnection":
        user = None
        if connection.user_id and connection.user_id in users:
            user = types.User._parse(client, users[connection.user_id])

        return BusinessConnection(
            client=client,
            id=connection.connection_id,
            user=user,
            dc_id=connection.dc_id,
            date=utils.timestamp_to_datetime(connection.date),
            can_reply=connection.can_reply or None,
            disabled=connection.disabled or None
        )
