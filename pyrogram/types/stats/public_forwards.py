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


class PublicForwards(Object):
    """Represents a list of public forwards.

    Parameters:
        count (``int``):
            Total number of forwards.

        forwards (List of :obj:`~pyrogram.types.PublicForward`):
            List of public forwards.

        next_offset (``str``, *optional*):
            Offset for the next page.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        count: int,
        forwards: List["types.PublicForward"],
        next_offset: str = None
    ):
        super().__init__(client)

        self.count = count
        self.forwards = forwards
        self.next_offset = next_offset

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        forwards: "raw.types.stats.PublicForwards"
    ) -> "PublicForwards":
        users = {u.id: u for u in forwards.users}
        chats = {c.id: c for c in forwards.chats}

        return PublicForwards(
            client=client,
            count=forwards.count,
            forwards=types.List([
                await types.PublicForward._parse(client, f, users, chats)
                for f in forwards.forwards
            ]),
            next_offset=forwards.next_offset
        )
