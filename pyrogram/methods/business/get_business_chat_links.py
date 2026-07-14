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

class GetBusinessChatLinks:
    async def get_business_chat_links(
        self: "pyrogram.Client"
    ) -> List["types.BusinessChatLink"]:
        """Get business chat links.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~pyrogram.types.BusinessChatLink`: On success, a list of business chat links is returned.
        """
        rpc = raw.functions.account.GetBusinessChatLinks()
        r = await self.invoke(rpc)

        return types.List([types.BusinessChatLink._parse(self, link) for link in r.links])
