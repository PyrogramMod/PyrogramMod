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

from typing import Optional

import pyrogram
from pyrogram import raw
from ..input_media.input_media import InputMedia


class InputMediaTodo(InputMedia):
    """Represents a to-do list to be sent.

    Parameters:
        title (``str``):
             Title of the to-do list.

        items (List of :obj:`~pyrogram.types.TodoItem`):
            List of to-do items.

    """

    def __init__(
        self,
        title: str,
        items: list
    ):
        super().__init__()

        self.title = title
        self.items = items

    async def write(self, client: "pyrogram.Client", next_file_id: int) -> "raw.types.InputMediaTodo":
        return raw.types.InputMediaTodo(
            title=self.title,
            items=[i.write() for i in self.items]
        )
