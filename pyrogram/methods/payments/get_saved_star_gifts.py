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

from typing import List, Union
import pyrogram
from pyrogram import raw, types

class GetSavedStarGifts:
    async def get_saved_star_gifts(
        self: "pyrogram.Client",
        peer: Union[int, str] = "me",
        offset: str = None,
        limit: int = 100
    ) -> List["types.StarGiftUnique"]:
        """Get the list of saved star gifts for a peer.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            peer (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the target chat.
                Defaults to "me" (your own saved gifts).

            offset (``str``, *optional*):
                Offset for pagination.

            limit (``int``, *optional*):
                Limit of results.

        Returns:
            List of :obj:`~pyrogram.types.StarGiftUnique`: On success, a list of unique star gifts is returned.
        """
        r = await self.invoke(
            raw.functions.payments.GetSavedStarGifts(
                peer=await self.resolve_peer(peer),
                offset=offset or "",
                limit=limit
            )
        )

        return types.List([
            types.StarGiftUnique._parse(self, gift)
            for gift in r.gifts
        ])
