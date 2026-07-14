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


class StoryReactionsList(Object):
    """Represents a list of story reactions.

    Parameters:
        count (``int``):
            Total number of reactions.

        reactions (List of :obj:`~pyrogram.types.StoryReaction`):
            List of story reactions.

        next_offset (``str``, *optional*):
            Offset for pagination.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        count: int,
        reactions: List["types.StoryReaction"],
        next_offset: str = None
    ):
        super().__init__(client)

        self.count = count
        self.reactions = reactions
        self.next_offset = next_offset

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        reactions_list: "raw.types.stories.StoryReactionsList"
    ) -> "StoryReactionsList":
        users = {u.id: u for u in reactions_list.users}
        chats = {c.id: c for c in reactions_list.chats}

        return StoryReactionsList(
            client=client,
            count=reactions_list.count,
            reactions=types.List([
                types.StoryReaction._parse(client, r, users, chats)
                for r in reactions_list.reactions
            ]),
            next_offset=reactions_list.next_offset
        )
