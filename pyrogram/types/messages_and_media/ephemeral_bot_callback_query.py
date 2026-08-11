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

from typing import Optional

import pyrogram
from pyrogram import raw
from pyrogram import types
from ..object import Object
from ..update import Update


class EphemeralBotCallbackQuery(Object, Update):
    """An ephemeral bot callback query update.

    Parameters:
        query_id (``int``):
            The query ID.

        user (:obj:`~pyrogram.types.User`):
            The user who pressed the button.

        message_id (``int``):
            The ephemeral message ID.

        data (``bytes``):
            The callback data.

        message (:obj:`~pyrogram.raw.base.EphemeralMessage`):
            The ephemeral message.

        chat_id (``int``, *optional*):
            The chat ID if available.

        chat_instance (``int``, *optional*):
            The chat instance identifier.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        query_id: int,
        user: "types.User",
        message_id: int,
        data: bytes,
        message: "raw.base.EphemeralMessage",
        chat_id: Optional[int] = None,
        chat_instance: Optional[int] = None,
    ):
        super().__init__(client)
        self.query_id = query_id
        self.user = user
        self.message_id = message_id
        self.data = data
        self.message = message
        self.chat_id = chat_id
        self.chat_instance = chat_instance

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        update: "raw.types.UpdateEphemeralBotCallbackQuery",
        users: dict
    ) -> "EphemeralBotCallbackQuery":
        user = types.User._parse(client, users.get(update.user_id))

        chat_id = None
        if update.peer:
            chat_id = pyrogram.utils.get_peer_id(update.peer)

        return EphemeralBotCallbackQuery(
            client=client,
            query_id=update.query_id,
            user=user,
            message_id=update.msg_id,
            data=update.data,
            message=update.message,
            chat_id=chat_id,
            chat_instance=update.chat_instance,
        )
