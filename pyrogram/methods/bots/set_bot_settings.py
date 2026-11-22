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

from typing import Union, Optional

import pyrogram
from pyrogram import raw, types


class SetBotSettings:
    async def set_bot_settings(
        self: "pyrogram.Client",
        bot: Optional[Union[int, str]] = None,
        inline_mode: Optional[bool] = None,
        inline_placeholder: Optional[str] = None,
        inline_geo: Optional[bool] = None,
        inline_feedback: Optional[int] = None,
        no_chats: Optional[bool] = None,
        chat_history: Optional[bool] = None,
        business: Optional[bool] = None,
        can_manage_bots: Optional[bool] = None,
        guest_chat: Optional[bool] = None,
        guard: Optional[bool] = None,
        forum_view: Optional[bool] = None,
        forum_can_manage_topics: Optional[bool] = None,
        forum_sidebar: Optional[bool] = None,
        bot_to_bot_communication_mode: Optional[bool] = None,
        callback_mode: Optional[str] = None
    ) -> "types.User":
        """Change the settings of a bot.

        Only the parameters that are not None are changed.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            bot (int | str, *optional*):
                Unique identifier (int) or username (str) of the bot.
                Pass None to change the settings of the current bot.

            inline_mode (bool, *optional*):
                Enable or disable inline mode.

            inline_placeholder (str, *optional*):
                Placeholder of the inline query input field.

            inline_geo (bool, *optional*):
                Request the user location with each inline query.

            inline_feedback (int, *optional*):
                Inline feedback (chosen inline result) sampling rate.

            no_chats (bool, *optional*):
                Disallow adding the bot to group chats (privacy: no chats).

            chat_history (bool, *optional*):
                Allow the bot to access the whole chat history (disable privacy mode).

            business (bool, *optional*):
                Allow the bot to be connected to business accounts.

            can_manage_bots (bool, *optional*):
                Allow the bot to manage other bots.

            guest_chat (bool, *optional*):
                Enable guest chat mode.

            guard (bool, *optional*):
                Enable guard bot mode.

            forum_view (bool, *optional*):
                Enable topics in private chats with the bot.

            forum_can_manage_topics (bool, *optional*):
                Allow users to manage topics in private chats with the bot.

            forum_sidebar (bool, *optional*):
                Show the topics of private chats in a sidebar.

            bot_to_bot_communication_mode (bool, *optional*):
                Enable bot-to-bot communication.

            callback_mode (str, *optional*):
                How callback queries are delivered.

        Returns:
            :obj:`~pyrogram.types.User`: The updated bot.

        Example:
            .. code-block:: python

                await app.set_bot_settings("@mybot", inline_mode=True, inline_placeholder="Search...")
        """
        r = await self.invoke(
            raw.functions.bots.SetBotSettings(
                bot=await self.resolve_peer(bot) if bot is not None else None,
                inline_mode=inline_mode,
                inline_placeholder=inline_placeholder,
                inline_geo=inline_geo,
                inline_feedback=inline_feedback,
                nochats=no_chats,
                chat_history=chat_history,
                business=business,
                can_manage_bots=can_manage_bots,
                guestchat=guest_chat,
                guard=guard,
                forum_view=forum_view,
                forum_can_manage_topics=forum_can_manage_topics,
                forum_sidebar=forum_sidebar,
                bot_to_bot_communication_mode=bot_to_bot_communication_mode,
                callback_mode=callback_mode
            )
        )

        return types.User._parse(self, r)
