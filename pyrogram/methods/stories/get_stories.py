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
from pyrogram import raw, types, utils


class GetStories:
    async def get_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_ids: Union[int, List[int]]
    ) -> Union["types.StoryItem", List["types.StoryItem"]]:
        """Get one or more stories by their IDs.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your own stories you can use "me" or "self".

            story_ids (``int`` | List of ``int``):
                Story ID or list of story IDs to get.

        Returns:
            :obj:`~pyrogram.types.StoryItem` | List of :obj:`~pyrogram.types.StoryItem`: On success,
            if a single story ID was passed, the story is returned, otherwise a list of stories is returned.

        Example:
            .. code-block:: python

                # Get a single story
                story = await app.get_stories(chat_id, 12345)

                # Get multiple stories
                stories = await app.get_stories(chat_id, [12345, 12346, 12347])
        """
        peer = await self.resolve_peer(chat_id)

        is_single = not isinstance(story_ids, list)
        story_ids = [story_ids] if is_single else story_ids

        r = await self.invoke(
            raw.functions.stories.GetStoriesByID(
                peer=peer,
                id=story_ids
            )
        )

        users = {u.id: u for u in r.users}
        chats = {c.id: c for c in r.chats}

        stories = []
        for story in r.stories:
            if isinstance(story, raw.types.StoryItem):
                stories.append(
                    await types.StoryItem._parse(self, story, users, chats, peer)
                )

        return stories[0] if is_single and stories else types.List(stories)
