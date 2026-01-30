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
from pyrogram import raw


class DeleteStories:
    async def delete_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_ids: Union[int, List[int]]
    ) -> List[int]:
        """Delete one or more stories.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your own stories you can use "me" or "self".

            story_ids (``int`` | List of ``int``):
                Story ID or list of story IDs to delete.

        Returns:
            List of ``int``: List of deleted story IDs.

        Example:
            .. code-block:: python

                # Delete a single story
                deleted = await app.delete_stories("me", 12345)

                # Delete multiple stories
                deleted = await app.delete_stories("me", [12345, 12346])
        """
        peer = await self.resolve_peer(chat_id)

        story_ids = [story_ids] if not isinstance(story_ids, list) else story_ids

        r = await self.invoke(
            raw.functions.stories.DeleteStories(
                peer=peer,
                id=story_ids
            )
        )

        return list(r)
