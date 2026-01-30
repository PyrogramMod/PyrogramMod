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


class UpdateSavedReactionTag:
    async def update_saved_reaction_tag(
        self: "pyrogram.Client",
        reaction: "types.Reaction",
        title: str = None
    ) -> bool:
        """Update a saved messages reaction tag.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            reaction (:obj:`~pyrogram.types.Reaction`):
                The reaction to update.

            title (``str``, *optional*):
                The new title for the tag.

        Returns:
            ``bool``: True on success.
        """
        return await self.invoke(
            raw.functions.messages.UpdateSavedReactionTag(
                reaction=await reaction.write(self),
                title=title
            )
        )
