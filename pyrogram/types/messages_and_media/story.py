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

import pyrogram
from pyrogram import raw
from ..object import Object


class Story(Object):
    """A Story.

    Parameters:
        peer: The peer of the story.
        chat_id: The chat ID of the story.
        via_mention: Whether the story is via mention.

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            peer,
            chat_id,
            via_mention,
    ):
        super().__init__(client)

        self.peer = peer
        self.chat_id = chat_id
        self.via_mention = via_mention

    @staticmethod
    def _parse(client, story: "raw.types.MessageMediaStory"):
        return Story(
            client=client,
            peer=story.peer,
            chat_id=story.id,
            via_mention=story.via_mention
        )
