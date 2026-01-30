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

class DeleteQuickReplyShortcut:
    async def delete_quick_reply_shortcut(
        self: "pyrogram.Client",
        shortcut_id: int
    ) -> bool:
        """Delete a quick reply shortcut.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            shortcut_id (``int``):
                The shortcut ID to delete.

        Returns:
            ``bool``: True on success.
        """
        return await self.invoke(
            raw.functions.messages.DeleteQuickReplyShortcut(
                shortcut_id=shortcut_id
            )
        )
