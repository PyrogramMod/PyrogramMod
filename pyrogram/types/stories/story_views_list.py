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
from ..object import Object


class StoryViewsList(Object):
    """Represents a list of story views.

    Parameters:
        count (``int``):
            Total number of views.

        views_count (``int``):
            Total number of views (including anonymous).

        forwards_count (``int``):
            Total number of forwards.

        reactions_count (``int``):
            Total number of reactions.

        views (List of :obj:`~pyrogram.types.StoryView`):
            List of story views.

        next_offset (``str``, *optional*):
            Offset for pagination.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        count: int,
        views_count: int,
        forwards_count: int,
        reactions_count: int,
        views: List["types.StoryView"],
        next_offset: str = None
    ):
        super().__init__(client)

        self.count = count
        self.views_count = views_count
        self.forwards_count = forwards_count
        self.reactions_count = reactions_count
        self.views = views
        self.next_offset = next_offset

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        views_list: "raw.types.stories.StoryViewsList"
    ) -> "StoryViewsList":
        users = {u.id: u for u in views_list.users}
        chats = {c.id: c for c in views_list.chats}

        return StoryViewsList(
            client=client,
            count=views_list.count,
            views_count=views_list.views_count,
            forwards_count=views_list.forwards_count,
            reactions_count=views_list.reactions_count,
            views=types.List([
                types.StoryView._parse(client, v, users, chats)
                for v in views_list.views
            ]),
            next_offset=views_list.next_offset
        )
