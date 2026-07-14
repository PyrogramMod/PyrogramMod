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

from typing import Union, List, Optional

import pyrogram
from pyrogram import raw, types


class ApplyBoost:
    async def apply_boost(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        slots: List[int] = None
    ) -> "types.BoostStatus":
        """Apply a boost to a channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target channel.
                You can also use channel public link in form of *t.me/<username>* (str).

            slots (List of ``int``, *optional*):
                Which of your boost slots to reassign to this channel.
                If not provided, the first available slot will be used.

        Returns:
            :obj:`~pyrogram.types.BoostStatus`: The updated boost status.

        Example:
            .. code-block:: python

                # Apply a boost to a channel
                status = await app.apply_boost(chat_id)
                print(f"New level: {status.level}")
        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.premium.ApplyBoost(
                peer=peer,
                slots=slots
            )
        )

        return types.BoostStatus._parse(self, r)
