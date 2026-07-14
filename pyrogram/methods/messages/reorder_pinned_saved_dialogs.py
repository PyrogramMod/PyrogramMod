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

from typing import List, Union
import pyrogram
from pyrogram import raw


class ReorderPinnedSavedDialogs:
    async def reorder_pinned_saved_dialogs(
        self: "pyrogram.Client",
        order: List[Union[int, str]],
        force: bool = None
    ) -> bool:
        """Reorder pinned saved messages dialogs.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            order (List of ``int`` | ``str``):
                The new order of pinned saved dialogs.

            force (``bool``, *optional*):
                Whether to force the reorder.

        Returns:
            ``bool``: True on success.
        """
        return await self.invoke(
            raw.functions.messages.ReorderPinnedSavedDialogs(
                order=[
                    raw.types.InputDialogPeer(peer=await self.resolve_peer(p))
                    for p in order
                ],
                force=force
            )
        )
