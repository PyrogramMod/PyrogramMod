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
from pyrogram import raw, types


class GetStarsStatus:
    async def get_stars_status(
        self: "pyrogram.Client",
        peer: Union[int, str] = None
    ) -> "types.StarsStatus":
        """Get the current Stars balance and subscription status.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            peer (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the peer to get status for.
                If not provided, gets your own Stars status.

        Returns:
            :obj:`~pyrogram.types.StarsStatus`: The Stars status.

        Example:
            .. code-block:: python

                # Get your own Stars status
                status = await app.get_stars_status()
                print(f"Balance: {status.balance}")

                # Get Stars status for a bot
                status = await app.get_stars_status("@mybot")
        """
        if peer:
            input_peer = await self.resolve_peer(peer)
        else:
            input_peer = raw.types.InputPeerSelf()

        r = await self.invoke(
            raw.functions.payments.GetStarsStatus(
                peer=input_peer
            )
        )

        return types.StarsStatus._parse(self, r)
