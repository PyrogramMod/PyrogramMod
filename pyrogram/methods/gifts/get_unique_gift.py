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

import pyrogram
from pyrogram import raw


class GetUniqueGift:
    async def get_unique_gift(
        self: "pyrogram.Client",
        slug: str
    ) -> "raw.types.payments.UniqueStarGift":
        """Get a unique (collectible) gift by its slug.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            slug (str):
                Slug of the gift, e.g. ``"PlushPepe-1"`` from ``t.me/nft/PlushPepe-1``.

        Returns:
            :obj:`~pyrogram.raw.types.payments.UniqueStarGift`: The raw gift with its chats and users.
            No high-level gift type exists yet.

        Example:
            .. code-block:: python

                r = await app.get_unique_gift("PlushPepe-1")
                print(r.gift.title, r.gift.num)
        """
        return await self.invoke(raw.functions.payments.GetUniqueStarGift(slug=slug))
