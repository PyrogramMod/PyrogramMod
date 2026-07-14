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


class DeleteQuickReplyMessages:
    async def delete_quick_reply_messages(
        self: "pyrogram.Client",
        shortcut_id: int,
        message_ids: List[int]
    ) -> "types.Updates":
        """Delete messages from a quick reply shortcut.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            shortcut_id (``int``):
                The shortcut ID.

            message_ids (List of ``int``):
                List of message IDs within the shortcut to delete.

        Returns:
            :obj:`~pyrogram.types.Updates`: On success, the updates object is returned.
        """
        return await self.invoke(
            raw.functions.messages.DeleteQuickReplyMessages(
                shortcut_id=shortcut_id,
                id=message_ids
            )
        )
