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


class ConfirmBotConnection:
    async def confirm_bot_connection(
        self: "pyrogram.Client",
        bot: Union[int, str]
    ) -> bool:
        """Confirm a new bot connection (e.g., from a new device or location).

        Called in response to an :obj:`~pyrogram.raw.types.UpdateNewBotConnection` update.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot (``int`` | ``str``):
                Unique identifier (int) or username (str) of the bot.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.confirm_bot_connection("@mybot")
        """

        peer = await self.resolve_peer(bot)
        if isinstance(peer, raw.types.InputPeerUser):
            input_user = raw.types.InputUser(user_id=peer.user_id, access_hash=peer.access_hash)
        else:
            input_user = peer

        return await self.invoke(
            raw.functions.account.ConfirmBotConnection(
                bot_id=input_user
            )
        )
