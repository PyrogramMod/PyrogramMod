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


class ToggleDirectMessages:
    async def toggle_direct_messages(
        self: "pyrogram.Client",
        channel_id: Union[int, str],
        enabled: bool,
        stars: int = 0,
    ) -> bool:
        """Enable or disable the monoforum (Direct Messages) for a broadcast channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            channel_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target channel.

            enabled (``bool``):
                Pass True to enable Direct Messages, False to disable.

            stars (``int``, *optional*):
                Number of Stars required to send a direct message. Defaults to 0 (free).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.toggle_direct_messages(channel_id, True)
        """
        await self.invoke(
            raw.functions.channels.UpdatePaidMessagesPrice(
                channel=await self.resolve_peer(channel_id),
                broadcast_messages_allowed=enabled,
                send_paid_messages_stars=stars
            )
        )

        return True
