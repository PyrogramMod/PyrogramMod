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
from pyrogram import raw, types


class GetUniqueStarGift:
    async def get_unique_star_gift(
        self: "pyrogram.Client",
        slug: str
    ) -> "types.StarGiftUnique":
        """Get information about a unique star gift by its slug.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            slug (``str``):
                The slug of the unique gift.

        Returns:
            :obj:`~pyrogram.types.StarGiftUnique`: On success, the unique star gift is returned.
        """
        r = await self.invoke(raw.functions.payments.GetUniqueStarGift(slug=slug))
        return types.StarGiftUnique._parse(self, r.gift)
