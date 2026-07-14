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

from typing import List
import pyrogram
from pyrogram import raw, types
from ..object import Object


class SavedDialogs(Object):
    """Represents a list of saved messages dialogs.

    Parameters:
        count (``int``):
            Total number of saved dialogs.

        dialogs (List of :obj:`~pyrogram.types.SavedDialog`):
            List of saved dialogs.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        count: int,
        dialogs: List["types.SavedDialog"]
    ):
        super().__init__(client)

        self.count = count
        self.dialogs = dialogs

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        saved_dialogs: "raw.base.messages.SavedDialogs"
    ) -> "SavedDialogs":
        users = {u.id: u for u in saved_dialogs.users}
        chats = {c.id: c for c in saved_dialogs.chats}

        messages = {
            m.id: await types.Message._parse(client, m, users, chats)
            for m in saved_dialogs.messages
        }

        return SavedDialogs(
            client=client,
            count=getattr(saved_dialogs, "count", len(saved_dialogs.dialogs)),
            dialogs=types.List([
                SavedDialog._parse(client, d, messages, users, chats)
                for d in saved_dialogs.dialogs
            ])
        )
