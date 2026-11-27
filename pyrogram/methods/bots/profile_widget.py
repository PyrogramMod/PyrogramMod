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
from pyrogram import raw


class ProfileWidget:
    async def edit_profile_widget_data(
        self: "pyrogram.Client",
        public_data: str,
        cache_time: Optional[int] = None
    ) -> bool:
        """Change the shared state of the widget on the bot's profile.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            public_data (``str``):
                New shared state, at most 1024 bytes.

            cache_time (``int``, *optional*):
                Seconds clients may cache *public_data*.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.edit_profile_widget_data("score:10", cache_time=60)
        """
        return await self.invoke(
            raw.functions.bots.EditProfileWidgetData(
                public_data=public_data,
                cache_time=cache_time
            )
        )

    async def edit_profile_widget_chat_data(
        self: "pyrogram.Client",
        user_id: Union[int, str],
        chat_data: str
    ) -> bool:
        """Change the state of the bot's profile widget for one user only.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the user.

            chat_data (``str``):
                New state for this user, at most 1024 bytes.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.edit_profile_widget_chat_data(user_id, "turn:2")
        """
        return await self.invoke(
            raw.functions.bots.EditProfileWidgetChatData(
                user_id=await self.resolve_peer(user_id),
                chat_data=chat_data
            )
        )

    async def get_profile_widget_public_data(
        self: "pyrogram.Client",
        bot_id: Union[int, str],
        hash: int = 0
    ) -> "raw.base.messages.WidgetPublicData":
        """Get the shared state of the widget on a bot's profile.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the bot.

            hash (``int``, *optional*):
                Hash of the state you already have; Telegram answers "not modified" if it is unchanged.

        Returns:
            :obj:`~pyrogram.raw.base.messages.WidgetPublicData`: The raw state with its hash and period.

        Example:
            .. code-block:: python

                r = await app.get_profile_widget_public_data("@mybot")
                print(r.data)
        """
        return await self.invoke(
            raw.functions.bots.GetProfileWidgetPublicData(
                bot=await self.resolve_peer(bot_id),
                hash=hash
            )
        )

    async def get_profile_widget_query_answer(
        self: "pyrogram.Client",
        bot_id: Union[int, str],
        data: Union[str, bytes],
        query_type: "raw.base.WidgetQueryType" = None
    ) -> Optional[str]:
        """Send a query to the widget on a bot's profile and wait for the bot's answer.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the bot.

            data (``str`` | ``bytes``):
                Data sent to the bot (1-64 bytes).

            query_type (:obj:`~pyrogram.raw.base.WidgetQueryType`, *optional*):
                Raw query type. Defaults to a plain data query.

        Returns:
            ``str``: The answer of the bot, or None if it answered nothing.

        Example:
            .. code-block:: python

                answer = await app.get_profile_widget_query_answer("@mybot", "ping")
        """
        r = await self.invoke(
            raw.functions.bots.GetProfileWidgetQueryAnswer(
                bot=await self.resolve_peer(bot_id),
                query_type=query_type or raw.types.WidgetQueryTypeData(),
                data=data.encode() if isinstance(data, str) else data
            )
        )

        return r.result
