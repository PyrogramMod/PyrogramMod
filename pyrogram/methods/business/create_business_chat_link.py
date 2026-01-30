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

class CreateBusinessChatLink:
    async def create_business_chat_link(
        self: "pyrogram.Client",
        link: "raw.types.InputBusinessChatLink"
    ) -> "types.BusinessChatLink":
        """Create a new business chat link.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            link (:obj:`~raw.types.InputBusinessChatLink`):
                The business chat link to create.

        Returns:
            :obj:`~pyrogram.types.BusinessChatLink`: On success, the created business chat link is returned.
        """
        rpc = raw.functions.account.CreateBusinessChatLink(
            link=link
        )
        r = await self.invoke(rpc)

        return types.BusinessChatLink._parse(self, r)
