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


class TodoList(Object):
    """Represents a to-do list attached to a message.

    Parameters:
        id (``int``):
            Unique identifier of the to-do list.

        title (``str``):
            Title of the to-do list.

        items (List of :obj:`~pyrogram.types.TodoItem`):
            List of to-do items.

        completions (List of :obj:`~pyrogram.types.TodoCompletion`, *optional*):
            List of completion entries.

        completed_count (``int``, *optional*):
            Number of completed items.

        total_count (``int``, *optional*):
            Total number of items.

        is_others_can_complete (``bool``, *optional*):
            Whether other users can mark items as complete.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int = None,
        title: str = None,
        items: List["types.TodoItem"] = None,
        completions: List["types.TodoCompletion"] = None,
        completed_count: int = None,
        total_count: int = None,
        is_others_can_complete: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.title = title
        self.items = items
        self.completions = completions
        self.completed_count = completed_count
        self.total_count = total_count
        self.is_others_can_complete = is_others_can_complete

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        todo: "raw.types.TodoList",
        users: dict = None
    ) -> "TodoList":
        users = users or {}

        items = []
        if hasattr(todo, 'list') and todo.list:
            items = [
                types.TodoItem._parse(client, item, users)
                for item in todo.list
            ]

        return TodoList(
            client=client,
            id=None,
            title=todo.title.text if hasattr(todo.title, 'text') else (todo.title if isinstance(todo.title, str) else None),
            items=types.List(items) if items else None,
            completions=None,
            completed_count=None,
            total_count=len(items) if items else None,
            is_others_can_complete=todo.others_can_complete if hasattr(todo, 'others_can_complete') else None
        )

    @staticmethod
    def _parse_media(
        client: "pyrogram.Client",
        media: "raw.types.MessageMediaToDo",
        users: dict = None
    ) -> "TodoList":
        """Parse from MessageMediaToDo which includes completions."""
        users = users or {}

        todo_list = TodoList._parse(client, media.todo, users) if media.todo else None

        if todo_list:
            completions = []
            if hasattr(media, 'completions') and media.completions:
                completions = [
                    types.TodoCompletion._parse(client, c, users)
                    for c in media.completions
                ]
            todo_list.completions = types.List(completions) if completions else None

            if completions:
                todo_list.completed_count = len(completions)

        return todo_list
