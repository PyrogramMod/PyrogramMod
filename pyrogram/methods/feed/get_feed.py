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
from pyrogram import raw


class GetFeed:
    async def get_feed(
        self: "pyrogram.Client",
        filter_id: int = 0,
        limit: int = 20,
        offset_position: "raw.types.FeedPosition" = None,
        add_offset: int = 0,
        max_position: "raw.types.FeedPosition" = None,
        min_position: "raw.types.FeedPosition" = None,
        offset_to_max_read: bool = None,
        hash: int = 0
    ) -> "raw.base.feed.FeedMessages":
        """Get posts of the news feed.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            filter_id (``int``, *optional*):
                Identifier of the feed folder. 0 for the main feed.

            limit (``int``, *optional*):
                Maximum number of posts to return.

            offset_position (:obj:`~pyrogram.raw.types.FeedPosition`, *optional*):
                Position to start from, e.g. ``min_position`` of the previous result.

            add_offset (``int``, *optional*):
                Extra offset from *offset_position*.

            max_position (:obj:`~pyrogram.raw.types.FeedPosition`, *optional*):
                Return only posts older than this position.

            min_position (:obj:`~pyrogram.raw.types.FeedPosition`, *optional*):
                Return only posts newer than this position.

            offset_to_max_read (``bool``, *optional*):
                Start from the last read post.

            hash (``int``, *optional*):
                Hash of the result you already have.

        Returns:
            :obj:`~pyrogram.raw.base.feed.FeedMessages`: The raw posts with their positions, chats and users.

        Example:
            .. code-block:: python

                r = await app.get_feed(limit=10)
                for m in r.messages:
                    print(m.id)
        """
        return await self.invoke(
            raw.functions.feed.GetFeed(
                filter_id=filter_id,
                add_offset=add_offset,
                limit=limit,
                hash=hash,
                offset_to_max_read=offset_to_max_read,
                offset_position=offset_position,
                max_position=max_position,
                min_position=min_position
            )
        )

    async def get_for_you_feed(
        self: "pyrogram.Client",
        limit: int = 20,
        query: Optional[str] = None
    ) -> "raw.types.feed.ForYouFeed":
        """Get the recommended "For You" feed.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            limit (``int``, *optional*):
                Maximum number of items to return.

            query (``str``, *optional*):
                Text to search for.

        Returns:
            :obj:`~pyrogram.raw.types.feed.ForYouFeed`: The raw feed items, chats, users and ``recommendation_id``.

        Example:
            .. code-block:: python

                r = await app.get_for_you_feed()
                print(len(r.items))
        """
        return await self.invoke(
            raw.functions.feed.GetForYou(limit=limit, query=query)
        )

    async def read_feed(
        self: "pyrogram.Client",
        max_position: "raw.types.FeedPosition",
        filter_id: int = 0
    ) -> bool:
        """Mark the news feed as read up to a position.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            max_position (:obj:`~pyrogram.raw.types.FeedPosition`):
                Last read position, e.g. ``max_position`` of :meth:`~pyrogram.Client.get_feed`.

            filter_id (``int``, *optional*):
                Identifier of the feed folder. 0 for the main feed.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                r = await app.get_feed()
                await app.read_feed(r.max_position)
        """
        await self.invoke(
            raw.functions.feed.ReadFeed(filter_id=filter_id, max_position=max_position)
        )

        return True
