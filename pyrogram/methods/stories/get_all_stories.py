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
from pyrogram import raw, types


class GetAllStories:
    async def get_all_stories(
        self: "pyrogram.Client",
        hidden: bool = False,
        next_offset: str = None
    ) -> List["types.PeerStories"]:
        """Get all active stories from followed users and channels.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            hidden (``bool``, *optional*):
                If True, get stories from hidden (archived) peers instead.

            next_offset (``str``, *optional*):
                Offset for pagination, returned from previous call.

        Returns:
            List of :obj:`~pyrogram.types.PeerStories`: On success, a list of peer stories is returned.

        Example:
            .. code-block:: python

                # Get all stories from followed users
                all_stories = await app.get_all_stories()

                for peer_stories in all_stories:
                    print(f"{peer_stories.peer} has {len(peer_stories.stories)} stories")
        """
        r = await self.invoke(
            raw.functions.stories.GetAllStories(
                hidden=hidden,
                next=next_offset is not None,
                state=next_offset or ""
            )
        )

        if isinstance(r, raw.types.stories.AllStoriesNotModified):
            return types.List([])

        users = {u.id: u for u in r.users}
        chats = {c.id: c for c in r.chats}

        peer_stories_list = []
        for peer_stories in r.peer_stories:
            parsed = await types.PeerStories._parse(self, peer_stories, users, chats)
            peer_stories_list.append(parsed)

        return types.List(peer_stories_list)
