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

from typing import List

import pyrogram
from pyrogram import raw, types
from ..object import Object


class MyBoosts(Object):
    """Represents a list of boosts applied by the current user.

    Parameters:
        my_boosts (List of :obj:`~pyrogram.types.MyBoost`):
            List of applied boosts.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        my_boosts: List["types.MyBoost"]
    ):
        super().__init__(client)

        self.my_boosts = my_boosts

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        boosts: "raw.types.premium.MyBoosts"
    ) -> "MyBoosts":
        users = {u.id: u for u in boosts.users}
        chats = {c.id: c for c in boosts.chats}

        return MyBoosts(
            client=client,
            my_boosts=types.List([
                types.MyBoost._parse(client, b, users, chats)
                for b in boosts.my_boosts
            ])
        )
