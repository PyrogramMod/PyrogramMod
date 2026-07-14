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

from datetime import datetime
from typing import Optional, List

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class TodoItem(Object):
    """Represents a single item in a to-do list.

    Parameters:
        id (``int``):
            Unique identifier of the to-do item.

        text (``str``):
            The text content of the to-do item.

        completed_by (:obj:`~pyrogram.types.User`, *optional*):
            The user who completed this item.

        completed_date (:py:obj:`~datetime.datetime`, *optional*):
            When the item was completed.

        is_completed (``bool``, *optional*):
            Whether this item is completed.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int = None,
        text: str = None,
        completed_by: "types.User" = None,
        completed_date: datetime = None,
        is_completed: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.text = text
        self.completed_by = completed_by
        self.completed_date = completed_date
        self.is_completed = is_completed

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        item: "raw.types.TodoItem",
        users: dict = None
    ) -> "TodoItem":
        completed_by = None
        if hasattr(item, 'completed_by') and item.completed_by and users:
            if item.completed_by in users:
                completed_by = types.User._parse(client, users[item.completed_by])

        return TodoItem(
            client=client,
            id=item.id,
            text=item.text,
            completed_by=completed_by,
            completed_date=utils.timestamp_to_datetime(item.completed_date) if hasattr(item, 'completed_date') and item.completed_date else None,
            is_completed=bool(completed_by or (hasattr(item, 'completed') and item.completed))
        )

    def write(self):
        return self.text
