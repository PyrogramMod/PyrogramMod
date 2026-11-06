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

from typing import Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object
from ..update import Update


class WidgetDataUpdate(Object, Update):
    """The state of a widget message changed.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Chat of the widget message.

        message_id (``int``):
            Identifier of the widget message.

        public_data (``str``, *optional*):
            New shared state, if it changed.

        chat_data (``str``, *optional*):
            New state of this message only, if it changed.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        chat: "types.Chat" = None,
        message_id: int,
        public_data: Optional[str] = None,
        chat_data: Optional[str] = None
    ):
        super().__init__(client)

        self.chat = chat
        self.message_id = message_id
        self.public_data = public_data
        self.chat_data = chat_data

    @staticmethod
    def _parse(client, update: "raw.types.UpdateMessageWidgetData", users, chats) -> "WidgetDataUpdate":
        return WidgetDataUpdate(
            chat=utils.parse_peer_chat(client, update.peer, users, chats),
            message_id=update.msg_id,
            public_data=update.public_data,
            chat_data=update.chat_data,
            client=client
        )
