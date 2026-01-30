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

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class StoryReaction(Object):
    """Represents a story reaction.

    Parameters:
        peer (:obj:`~pyrogram.types.Chat` | :obj:`~pyrogram.types.User`):
            The peer who reacted to the story.

        date (``datetime``):
            Date when the reaction was sent.

        reaction (:obj:`~pyrogram.types.Reaction`):
            The reaction itself.

        message (:obj:`~pyrogram.types.Message`, *optional*):
            The message if it's a public forward.

        story (:obj:`~pyrogram.types.StoryItem`, *optional*):
            The reposted story.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        peer: "types.Chat" = None,
        date: datetime = None,
        reaction: "types.Reaction" = None,
        message: "types.Message" = None,
        story: "types.StoryItem" = None
    ):
        super().__init__(client)

        self.peer = peer
        self.date = date
        self.reaction = reaction
        self.message = message
        self.story = story

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        reaction: "raw.base.StoryReaction",
        users: dict = None,
        chats: dict = None
    ) -> "StoryReaction":
        if isinstance(reaction, raw.types.StoryReaction):
            return StoryReaction(
                client=client,
                peer=types.Chat._parse(client, reaction.peer_id, users, chats),
                date=utils.timestamp_to_datetime(reaction.date),
                reaction=types.Reaction._parse(client, reaction.reaction)
            )

        if isinstance(reaction, raw.types.StoryReactionPublicForward):
            return StoryReaction(
                client=client,
                message=types.Message._parse(client, reaction.message, users, chats)
            )

        if isinstance(reaction, raw.types.StoryReactionPublicRepost):
            return StoryReaction(
                client=client,
                peer=types.Chat._parse(client, reaction.peer_id, users, chats),
                story=types.StoryItem._parse(client, reaction.story)
            )
