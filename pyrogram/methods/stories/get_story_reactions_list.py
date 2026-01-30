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

from typing import Union
import pyrogram
from pyrogram import raw, types

class GetStoryReactionsList:
    async def get_story_reactions_list(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_id: int,
        reaction: "types.Reaction" = None,
        forwards_first: bool = None,
        offset: str = None,
        limit: int = 20
    ) -> "types.StoryReactionsList":
        """Get the list of reactions on a story.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            story_id (``int``):
                The story ID.

            reaction (:obj:`~pyrogram.types.Reaction`, *optional*):
                Filter by a specific reaction.

            forwards_first (``bool``, *optional*):
                Pass True to get forwards first.

            offset (``str``, *optional*):
                Offset for pagination.

            limit (``int``, *optional*):
                Limit of results.

        Returns:
            :obj:`~pyrogram.types.StoryReactionsList`: The list of story reactions.
        """
        rpc = raw.functions.stories.GetStoryReactionsList(
            peer=await self.resolve_peer(chat_id),
            id=story_id,
            reaction=await reaction.write(self) if reaction else None,
            forwards_first=forwards_first,
            offset=offset or "",
            limit=limit
        )
        r = await self.invoke(rpc)

        return types.StoryReactionsList._parse(self, r)
