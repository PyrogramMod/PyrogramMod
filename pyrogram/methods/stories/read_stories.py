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


class ReadStories:
    async def read_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        max_id: int
    ) -> List[int]:
        """Mark stories as read up to a certain ID.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            max_id (``int``):
                The ID of the last story to mark as read.
                All stories with ID <= max_id will be marked as read.

        Returns:
            List of ``int``: List of story IDs that were marked as read.

        Example:
            .. code-block:: python

                # Mark all stories up to ID 12345 as read
                read_ids = await app.read_stories("username", 12345)
        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.stories.ReadStories(
                peer=peer,
                max_id=max_id
            )
        )

        return list(r)
