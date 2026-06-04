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

from typing import Union, Optional, List

import pyrogram
from pyrogram import raw


class EditBotAccessSettings:
    async def edit_bot_access_settings(
        self: "pyrogram.Client",
        bot: Union[int, str],
        restricted: Optional[bool] = None,
        add_users: Optional[List[Union[int, str]]] = None
    ) -> bool:
        """Edit the access settings of a bot.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot (``int`` | ``str``):
                Unique identifier (int) or username (str) of the bot.

            restricted (``bool``, *optional*):
                Pass True to restrict the bot's access.

            add_users (List of ``int`` | ``str``, *optional*):
                List of users to grant access to the bot.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Restrict bot
                await app.edit_bot_access_settings("@mybot", restricted=True)

                # Allow specific users
                await app.edit_bot_access_settings("@mybot", add_users=["@user1", "@user2"])
        """

        resolved_users = None
        if add_users is not None:
            resolved_users = [await self.resolve_peer(u) for u in add_users]

        await self.invoke(
            raw.functions.bots.EditAccessSettings(
                bot=await self.resolve_peer(bot),
                restricted=restricted,
                add_users=resolved_users
            )
        )

        return True
