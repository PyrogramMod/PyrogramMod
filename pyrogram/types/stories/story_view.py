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


class StoryView(Object):
    """Represents a story view.

    Parameters:
        user (:obj:`~pyrogram.types.User`, *optional*):
            The user who viewed the story.

        date (``datetime``, *optional*):
            Date when the story was viewed.

        reaction (:obj:`~pyrogram.types.Reaction`, *optional*):
            Reaction sent by the user.

        message (:obj:`~pyrogram.types.Message`, *optional*):
            The message if it's a public forward.

        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            The chat where the story was reposted.

        story (:obj:`~pyrogram.types.StoryItem`, *optional*):
            The reposted story.

        blocked (``bool``, *optional*):
            Whether the user is blocked from viewing stories.

        blocked_my_stories_from (``bool``, *optional*):
            Whether the user is blocked from viewing my stories.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        user: "types.User" = None,
        date: datetime = None,
        reaction: "types.Reaction" = None,
        message: "types.Message" = None,
        chat: "types.Chat" = None,
        story: "types.StoryItem" = None,
        blocked: bool = None,
        blocked_my_stories_from: bool = None
    ):
        super().__init__(client)

        self.user = user
        self.date = date
        self.reaction = reaction
        self.message = message
        self.chat = chat
        self.story = story
        self.blocked = blocked
        self.blocked_my_stories_from = blocked_my_stories_from

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        view: "raw.base.StoryView",
        users: dict = None,
        chats: dict = None
    ) -> "StoryView":
        if isinstance(view, raw.types.StoryView):
            return StoryView(
                client=client,
                user=types.User._parse(client, users.get(view.user_id)) if users else None,
                date=utils.timestamp_to_datetime(view.date),
                reaction=types.Reaction._parse(client, view.reaction) if view.reaction else None,
                blocked=view.blocked,
                blocked_my_stories_from=view.blocked_my_stories_from
            )

        if isinstance(view, raw.types.StoryViewPublicForward):
            return StoryView(
                client=client,
                message=types.Message._parse(client, view.message, users, chats),
                blocked=view.blocked,
                blocked_my_stories_from=view.blocked_my_stories_from
            )

        if isinstance(view, raw.types.StoryViewPublicRepost):
            return StoryView(
                client=client,
                chat=types.Chat._parse(client, view.peer_id, users, chats),
                story=types.StoryItem._parse(client, view.story),
                blocked=view.blocked,
                blocked_my_stories_from=view.blocked_my_stories_from
            )
