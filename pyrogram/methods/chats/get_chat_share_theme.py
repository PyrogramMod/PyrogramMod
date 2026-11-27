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

from typing import Union

import pyrogram
from pyrogram import raw


class GetChatShareTheme:
    async def get_chat_share_theme(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> "raw.base.ShareTheme":
        """Get the theme shown on the link-sharing screen of a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (int | str):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            :obj:`~pyrogram.raw.base.ShareTheme`: The raw theme: default, emoji backdrop or gift.

        Example:
            .. code-block:: python

                theme = await app.get_chat_share_theme(chat_id)
        """
        return await self.invoke(
            raw.functions.messages.GetShareTheme(
                peer=await self.resolve_peer(chat_id)
            )
        )
