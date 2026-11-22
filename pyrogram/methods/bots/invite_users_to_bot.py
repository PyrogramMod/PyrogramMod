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

from typing import Union, List

import pyrogram
from pyrogram import raw


class InviteUsersToBot:
    async def invite_users_to_bot(
        self: "pyrogram.Client",
        bot: Union[int, str],
        user_ids: List[Union[int, str]]
    ) -> bool:
        """Invite up to 10 users to a private chat with a bot you own.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot (int | str):
                Unique identifier (int) or username (str) of the bot.

            user_ids (List of int | str):
                Users to invite, at most 10.

        Returns:
            bool: True on success.

        Example:
            .. code-block:: python

                await app.invite_users_to_bot("@mybot", ["@user1", "@user2"])
        """
        if not 1 <= len(user_ids) <= 10:
            raise ValueError("user_ids must contain between 1 and 10 users")

        return await self.invoke(
            raw.functions.messages.InviteUsersToBot(
                bot=await self.resolve_peer(bot),
                users=[await self.resolve_peer(u) for u in user_ids]
            )
        )
