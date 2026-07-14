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

from typing import List, Optional, Union

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class PeerStories(Object):
    """Stories associated with a peer.

    Parameters:
        peer (:obj:`~pyrogram.types.User` | :obj:`~pyrogram.types.Chat`):
            The peer (user or chat) these stories belong to.

        stories (List of :obj:`~pyrogram.types.StoryItem`):
            List of stories.

        max_read_id (``int``, *optional*):
            The ID of the last read story.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        peer: Union["types.User", "types.Chat"] = None,
        stories: List["types.StoryItem"] = None,
        max_read_id: int = None
    ):
        super().__init__(client)

        self.peer = peer
        self.stories = stories
        self.max_read_id = max_read_id

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        peer_stories: "raw.types.PeerStories",
        users: dict,
        chats: dict
    ) -> "PeerStories":
        from pyrogram.types.stories import StoryItem

        # Parse the peer
        peer = None
        if isinstance(peer_stories.peer, raw.types.PeerUser):
            peer = types.User._parse(client, users.get(peer_stories.peer.user_id))
        elif isinstance(peer_stories.peer, raw.types.PeerChannel):
            peer = types.Chat._parse_channel_chat(client, chats.get(peer_stories.peer.channel_id))
        elif isinstance(peer_stories.peer, raw.types.PeerChat):
            peer = types.Chat._parse_chat_chat(client, chats.get(peer_stories.peer.chat_id))

        # Parse stories
        stories = []
        for story in peer_stories.stories:
            if isinstance(story, raw.types.StoryItem):
                parsed_story = await StoryItem._parse(
                    client, story, users, chats, peer_stories.peer
                )
                stories.append(parsed_story)

        return PeerStories(
            client=client,
            peer=peer,
            stories=types.List(stories) if stories else None,
            max_read_id=peer_stories.max_read_id
        )
