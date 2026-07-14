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
from typing import Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class TodoCompletion(Object):
    """Represents a completion entry for a to-do item.

    Parameters:
        item_id (``int``):
            The ID of the to-do item.

        user (:obj:`~pyrogram.types.User`):
            The user who completed this item.

        date (:py:obj:`~datetime.datetime`):
            When the item was completed.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        item_id: int = None,
        user: "types.User" = None,
        date: datetime = None
    ):
        super().__init__(client)

        self.item_id = item_id
        self.user = user
        self.date = date

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        completion: "raw.types.TodoCompletion",
        users: dict
    ) -> "TodoCompletion":
        user = None
        if completion.user_id and completion.user_id in users:
            user = types.User._parse(client, users[completion.user_id])

        return TodoCompletion(
            client=client,
            item_id=completion.item_id,
            user=user,
            date=utils.timestamp_to_datetime(completion.date) if hasattr(completion, 'date') and completion.date else None
        )
