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
from pyrogram import raw, types
from ..object import Object


class SavedReactionTag(Object):
    """Represents a saved messages reaction tag.

    Parameters:
        reaction (:obj:`~pyrogram.types.Reaction`):
            The reaction.

        title (``str``, *optional*):
            The title of the tag.

        count (``int``):
            Number of messages with this tag.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        reaction: "types.Reaction",
        title: str = None,
        count: int
    ):
        super().__init__(client)

        self.reaction = reaction
        self.title = title
        self.count = count

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        tag: "raw.types.SavedReactionTag"
    ) -> "SavedReactionTag":
        return SavedReactionTag(
            client=client,
            reaction=types.Reaction._parse(client, tag.reaction),
            title=getattr(tag, "title", None),
            count=tag.count
        )
