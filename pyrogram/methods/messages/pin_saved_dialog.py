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

class PinSavedDialog:
    async def pin_saved_dialog(
        self: "pyrogram.Client",
        peer: Union[int, str],
        pinned: bool = True
    ) -> bool:
        """Pin or unpin a saved messages dialog.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            peer (``int`` | ``str``):
                Unique identifier (int) or username (str) of the chat.

            pinned (``bool``, *optional*):
                Whether to pin or unpin the dialog. Defaults to True (pin).

        Returns:
            ``bool``: True on success.
        """
        return await self.invoke(
            raw.functions.messages.ToggleSavedDialogPin(
                peer=raw.types.InputDialogPeer(
                    peer=await self.resolve_peer(peer)
                ),
                pinned=pinned
            )
        )
