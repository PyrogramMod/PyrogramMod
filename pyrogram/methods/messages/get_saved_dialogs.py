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

class GetSavedDialogs:
    async def get_saved_dialogs(
        self: "pyrogram.Client",
        offset_date: int = 0,
        offset_id: int = 0,
        offset_peer: Union[int, str] = None,
        limit: int = 100
    ) -> "types.SavedDialogs":
        """Get the list of saved messages dialogs.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            offset_date (``int``, *optional*):
                Offset date for pagination.

            offset_id (``int``, *optional*):
                Offset message ID for pagination.

            offset_peer (``int`` | ``str``, *optional*):
                Offset peer for pagination.

            limit (``int``, *optional*):
                Limit of results.

        Returns:
            :obj:`~pyrogram.types.SavedDialogs`: On success, the saved dialogs are returned.
        """
        rpc = raw.functions.messages.GetSavedDialogs(
            offset_date=offset_date,
            offset_id=offset_id,
            offset_peer=await self.resolve_peer(offset_peer or raw.types.InputPeerEmpty()),
            limit=limit,
            hash=0
        )
        r = await self.invoke(rpc)

        return await types.SavedDialogs._parse(self, r)
