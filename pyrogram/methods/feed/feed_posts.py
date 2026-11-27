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


class FeedPosts:
    async def like_post(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int
    ) -> bool:
        """Like a post of the feed.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the channel.

            message_id (``int``):
                Identifier of the post.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.like_post(chat_id, message_id)
        """
        return await self.invoke(
            raw.functions.feed.LikePost(peer=await self.resolve_peer(chat_id), msg_id=message_id)
        )

    async def dislike_post(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int
    ) -> bool:
        """Dislike a post of the feed, so that fewer similar posts are shown.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the channel.

            message_id (``int``):
                Identifier of the post.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.dislike_post(chat_id, message_id)
        """
        return await self.invoke(
            raw.functions.feed.DislikePost(peer=await self.resolve_peer(chat_id), msg_id=message_id)
        )

    async def report_feed_events(
        self: "pyrogram.Client",
        events: List["raw.types.InputFeedEvent"]
    ) -> bool:
        """Send feed events (views, clicks and so on) to Telegram.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            events (List of :obj:`~pyrogram.raw.types.InputFeedEvent`):
                Raw events to send.

        Returns:
            ``bool``: True on success.
        """
        return await self.invoke(raw.functions.messages.ReportFeedEvents(events=events))
