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

class GetMyBoosts:
    async def get_my_boosts(
        self: "pyrogram.Client"
    ) -> "types.MyBoosts":
        """Get the list of your own boosts.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            :obj:`~pyrogram.types.MyBoosts`: The list of your boosts.
        """
        r = await self.invoke(raw.functions.premium.GetMyBoosts())
        return types.MyBoosts._parse(self, r)
