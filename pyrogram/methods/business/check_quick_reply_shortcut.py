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


class CheckQuickReplyShortcut:
    async def check_quick_reply_shortcut(
        self: "pyrogram.Client",
        shortcut: str
    ) -> bool:
        """Check if a quick reply shortcut name is available.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            shortcut (``str``):
                The shortcut name to check.

        Returns:
            ``bool``: True if available.
        """
        return await self.invoke(
            raw.functions.messages.CheckQuickReplyShortcut(
                shortcut=shortcut
            )
        )
