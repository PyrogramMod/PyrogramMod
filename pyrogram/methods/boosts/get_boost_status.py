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


class GetBoostStatus:
    async def get_boost_status(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> "types.BoostStatus":
        """Get boost status for a channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target channel.
                You can also use channel public link in form of *t.me/<username>* (str).

        Returns:
            :obj:`~pyrogram.types.BoostStatus`: On success, the boost status is returned.

        Example:
            .. code-block:: python

                status = await app.get_boost_status(chat_id)
                print(f"Level: {status.level}, Boosts: {status.boosts}")
        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.premium.GetBoostsStatus(
                peer=peer
            )
        )

        return types.BoostStatus._parse(self, r)
