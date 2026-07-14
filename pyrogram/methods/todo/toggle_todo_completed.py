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

from typing import List, Union
import pyrogram
from pyrogram import raw, types

class ToggleTodoCompleted:
    async def toggle_todo_completed(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        completed: List[int] = None,
        incompleted: List[int] = None
    ) -> "types.Updates":
        """Toggle to-do items as completed or incompleted.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the message containing the to-do list.

            completed (List of ``int``, *optional*):
                List of item indices to mark as completed.

            incompleted (List of ``int``, *optional*):
                List of item indices to mark as incompleted.

        Returns:
            :obj:`~pyrogram.types.Updates`: On success, the updates object is returned.
        """
        return await self.invoke(
            raw.functions.messages.ToggleTodoCompleted(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                completed=completed or [],
                incompleted=incompleted or []
            )
        )
