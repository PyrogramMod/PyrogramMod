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

from typing import List, Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class StoryViews(Object):
    """Aggregated view and reaction information of a story.

    Parameters:
        views_count (``int``):
            View counter of the story.

        has_viewers (``bool``, *optional*):
            Whether the viewers list is currently viewable.

        forwards_count (``int``, *optional*):
            Forward counter of the story.

        reactions (List of :obj:`~pyrogram.types.Reaction`, *optional*):
            All reactions added to this story.

        reactions_count (``int``, *optional*):
            Number of reactions added to the story.

        recent_viewers (List of ``int``, *optional*):
            User IDs of some recent viewers of the story.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        views_count: int,
        has_viewers: bool = None,
        forwards_count: int = None,
        reactions: List["types.Reaction"] = None,
        reactions_count: int = None,
        recent_viewers: List[int] = None
    ):
        super().__init__(client)

        self.views_count = views_count
        self.has_viewers = has_viewers
        self.forwards_count = forwards_count
        self.reactions = reactions
        self.reactions_count = reactions_count
        self.recent_viewers = recent_viewers

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        story_views: "raw.types.StoryViews"
    ) -> "StoryViews":
        reactions = None
        if story_views.reactions:
            reactions = [
                types.Reaction._parse(client, r.reaction)
                for r in story_views.reactions
            ]

        return StoryViews(
            client=client,
            views_count=story_views.views_count,
            has_viewers=story_views.has_viewers or None,
            forwards_count=story_views.forwards_count,
            reactions=types.List(reactions) if reactions else None,
            reactions_count=story_views.reactions_count,
            recent_viewers=types.List(story_views.recent_viewers) if story_views.recent_viewers else None
        )
