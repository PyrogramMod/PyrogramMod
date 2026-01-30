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


class BoostsList(Object):
    """List of boosts.

    Parameters:
        count (``int``):
            Total number of boosts.

        boosts (List of :obj:`~pyrogram.types.Boost`):
            List of boosts.

        next_offset (``str``, *optional*):
            Offset for pagination.

        users (List of :obj:`~pyrogram.types.User`, *optional*):
            List of users mentioned in the boosts.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        count: int,
        boosts: List["types.Boost"],
        next_offset: str = None,
        users: List["types.User"] = None
    ):
        super().__init__(client)

        self.count = count
        self.boosts = boosts
        self.next_offset = next_offset
        self.users = users

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        boosts_list: "raw.types.premium.BoostsList",
    ) -> "BoostsList":
        users = {u.id: u for u in boosts_list.users}

        return BoostsList(
            client=client,
            count=boosts_list.count,
            boosts=types.List([
                types.Boost._parse(client, boost, users)
                for boost in boosts_list.boosts
            ]),
            next_offset=boosts_list.next_offset,
            users=types.List([
                types.User._parse(client, user)
                for user in boosts_list.users
            ])
        )
