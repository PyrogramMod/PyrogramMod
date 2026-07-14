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

class EditBusinessChatLink:
    async def edit_business_chat_link(
        self: "pyrogram.Client",
        slug: str,
        link: "raw.types.InputBusinessChatLink"
    ) -> "types.BusinessChatLink":
        """Edit an existing business chat link.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            slug (``str``):
                The slug of the link to edit.

            link (:obj:`~raw.types.InputBusinessChatLink`):
                The new business chat link details.

        Returns:
            :obj:`~pyrogram.types.BusinessChatLink`: On success, the edited business chat link is returned.
        """
        rpc = raw.functions.account.EditBusinessChatLink(
            slug=slug,
            link=link
        )
        r = await self.invoke(rpc)

        return types.BusinessChatLink._parse(self, r)
