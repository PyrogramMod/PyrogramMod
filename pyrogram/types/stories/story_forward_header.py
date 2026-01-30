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

from typing import Optional

import pyrogram
from pyrogram import raw, utils
from ..object import Object


class StoryForwardHeader(Object):
    """Contains information about the original story that was reposted.

    Parameters:
        from_peer_id (``int``, *optional*):
            ID of the peer that originally posted this story.

        from_name (``str``, *optional*):
            For stories forwarded from users who have hidden their account,
            the name of the original poster.

        story_id (``int``, *optional*):
            ID of the original story.

        is_modified (``bool``, *optional*):
            Whether this story was modified when reposted.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        from_peer_id: int = None,
        from_name: str = None,
        story_id: int = None,
        is_modified: bool = None
    ):
        super().__init__(client)

        self.from_peer_id = from_peer_id
        self.from_name = from_name
        self.story_id = story_id
        self.is_modified = is_modified

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        fwd_header: "raw.types.StoryFwdHeader"
    ) -> Optional["StoryForwardHeader"]:
        if fwd_header is None:
            return None

        from_peer_id = None
        if fwd_header.from_:
            from_peer_id = utils.get_peer_id(fwd_header.from_)

        return StoryForwardHeader(
            client=client,
            from_peer_id=from_peer_id,
            from_name=fwd_header.from_name,
            story_id=fwd_header.story_id,
            is_modified=fwd_header.modified or None
        )
