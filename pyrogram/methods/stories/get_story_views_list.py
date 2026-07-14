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

class GetStoryViewsList:
    async def get_story_views_list(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_id: int,
        query: str = None,
        just_contacts: bool = None,
        reactions_first: bool = None,
        forwards_first: bool = None,
        offset: str = None,
        limit: int = 20
    ) -> "types.StoryViewsList":
        """Get the list of viewers of a story.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            story_id (``int``):
                The story ID.

            query (``str``, *optional*):
                Search query to filter viewers by name.

            just_contacts (``bool``, *optional*):
                Pass True to only get contacts.

            reactions_first (``bool``, *optional*):
                Pass True to get viewers who reacted first.

            forwards_first (``bool``, *optional*):
                Pass True to get viewers who forwarded first.

            offset (``str``, *optional*):
                Offset for pagination.

            limit (``int``, *optional*):
                Limit of results.

        Returns:
            :obj:`~pyrogram.types.StoryViewsList`: The list of story views.
        """
        rpc = raw.functions.stories.GetStoryViewsList(
            peer=await self.resolve_peer(chat_id),
            id=story_id,
            q=query or "",
            just_contacts=just_contacts,
            reactions_first=reactions_first,
            forwards_first=forwards_first,
            offset=offset or "",
            limit=limit
        )
        r = await self.invoke(rpc)

        return types.StoryViewsList._parse(self, r)
