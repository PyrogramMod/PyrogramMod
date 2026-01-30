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


class MyBoost(Object):
    """Represents a boost applied by the current user.

    Parameters:
        slot (``int``):
            The boost slot identifier.

        peer (:obj:`~pyrogram.types.Chat`, *optional*):
            The chat where the boost is applied.

        date (``datetime``):
            Date when the boost was applied.

        expires (``datetime``):
            Date when the boost will expire.

        cooldown_until_date (``datetime``, *optional*):
            Date until which the boost slot is on cooldown.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        slot: int,
        peer: "types.Chat" = None,
        date: datetime,
        expires: datetime,
        cooldown_until_date: datetime = None
    ):
        super().__init__(client)

        self.slot = slot
        self.peer = peer
        self.date = date
        self.expires = expires
        self.cooldown_until_date = cooldown_until_date

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        boost: "raw.types.MyBoost",
        users: dict = None,
        chats: dict = None
    ) -> "MyBoost":
        return MyBoost(
            client=client,
            slot=boost.slot,
            peer=types.Chat._parse(client, boost.peer, users, chats) if boost.peer else None,
            date=utils.timestamp_to_datetime(boost.date),
            expires=utils.timestamp_to_datetime(boost.expires),
            cooldown_until_date=utils.timestamp_to_datetime(boost.cooldown_until_date) if boost.cooldown_until_date else None
        )
