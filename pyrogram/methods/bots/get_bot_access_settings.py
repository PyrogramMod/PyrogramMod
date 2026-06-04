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

from typing import Union

import pyrogram
from pyrogram import raw


class GetBotAccessSettings:
    async def get_bot_access_settings(
        self: "pyrogram.Client",
        bot: Union[int, str]
    ) -> "raw.types.bots.AccessSettings":
        """Get the access settings of a bot.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot (``int`` | ``str``):
                Unique identifier (int) or username (str) of the bot.

        Returns:
            :obj:`~pyrogram.raw.types.bots.AccessSettings`: The bot access settings.

        Example:
            .. code-block:: python

                settings = await app.get_bot_access_settings("@mybot")
                print(settings.restricted, settings.add_users)
        """

        return await self.invoke(
            raw.functions.bots.GetAccessSettings(
                bot=await self.resolve_peer(bot)
            )
        )
