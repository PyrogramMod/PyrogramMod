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
from pyrogram import raw, types

class GetSavedReactionTags:
    async def get_saved_reaction_tags(
        self: "pyrogram.Client",
        peer: Union[int, str] = None
    ) -> List["types.SavedReactionTag"]:
        """Get reaction tags used in saved messages.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            peer (``int`` | ``str``, *optional*):
                Filter by a specific chat.

        Returns:
            List of :obj:`~pyrogram.types.SavedReactionTag`: On success, a list of reaction tags is returned.
        """
        r = await self.invoke(
            raw.functions.messages.GetSavedReactionTags(
                peer=await self.resolve_peer(peer) if peer else None,
                hash=0
            )
        )

        return types.List([
            types.SavedReactionTag._parse(self, tag)
            for tag in r.tags
        ])
