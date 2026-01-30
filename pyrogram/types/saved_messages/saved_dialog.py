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

import pyrogram
from pyrogram import raw, types
from ..object import Object


class SavedDialog(Object):
    """Represents a saved messages dialog.

    Parameters:
        peer (:obj:`~pyrogram.types.Chat` | :obj:`~pyrogram.types.User`):
            The peer of the saved dialog.

        top_message (:obj:`~pyrogram.types.Message`):
            The top message of the saved dialog.

        pinned (``bool``, *optional*):
            Whether the dialog is pinned.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        peer: "types.Chat" = None,
        top_message: "types.Message" = None,
        pinned: bool = None
    ):
        super().__init__(client)

        self.peer = peer
        self.top_message = top_message
        self.pinned = pinned

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        dialog: "raw.types.SavedDialog",
        messages: dict,
        users: dict,
        chats: dict
    ) -> "SavedDialog":
        return SavedDialog(
            client=client,
            peer=types.Chat._parse(client, dialog.peer, users, chats),
            top_message=messages.get(dialog.top_message),
            pinned=getattr(dialog, "pinned", None)
        )

    async def pin(self) -> bool:
        """Bound method *pin* of :obj:`~pyrogram.types.SavedDialog`.

        Use as a shortcut for:
            .. code-block:: python

                await dialog.pin()

        Returns:
            ``bool``: True on success.
        """
        return await self._client.pin_saved_dialog(peer=self.peer.id, pinned=True)

    async def unpin(self) -> bool:
        """Bound method *unpin* of :obj:`~pyrogram.types.SavedDialog`.

        Use as a shortcut for:
            .. code-block:: python

                await dialog.unpin()

        Returns:
            ``bool``: True on success.
        """
        return await self._client.pin_saved_dialog(peer=self.peer.id, pinned=False)
