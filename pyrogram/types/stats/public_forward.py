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

from typing import Optional, Union

import pyrogram
from pyrogram import raw, types
from ..object import Object


class PublicForward(Object):
    """Represents a public forward.

    Parameters:
        message (:obj:`~pyrogram.types.Message`, *optional*):
            The message if it's a message forward.

        story (:obj:`~pyrogram.types.StoryItem`, *optional*):
            The story if it's a story forward.

        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            The chat where the story was forwarded.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        message: "types.Message" = None,
        story: "types.StoryItem" = None,
        chat: "types.Chat" = None
    ):
        super().__init__(client)

        self.message = message
        self.story = story
        self.chat = chat

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        forward: "raw.base.PublicForward",
        users: dict,
        chats: dict
    ) -> "PublicForward":
        if isinstance(forward, raw.types.PublicForwardMessage):
            return PublicForward(
                client=client,
                message=await types.Message._parse(client, forward.message, users, chats)
            )

        if isinstance(forward, raw.types.PublicForwardStory):
            return PublicForward(
                client=client,
                chat=types.Chat._parse(client, forward.peer, users, chats),
                story=types.StoryItem._parse(client, forward.story)
            )
