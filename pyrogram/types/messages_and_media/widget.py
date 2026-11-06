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

import zlib
from typing import Optional

import pyrogram
from pyrogram import raw
from ..object import Object


class Widget(Object):
    """A widget: a self-contained HTML document drawn inside the message bubble.

    Parameters:
        html (``str``):
            The widget's HTML document.

        width (``int``):
            Width size anchor of the bubble in points, 0 means auto.

        height (``int``):
            Height size anchor of the bubble in points, 0 means auto.

        public_data (``str``, *optional*):
            State shared by every copy of a shared widget (at most 1024 bytes).

        chat_data (``str``, *optional*):
            State of this message only (at most 1024 bytes).

        id (``int``, *optional*):
            Identifier of the shared widget. Present only for shared widgets.

        is_copy (``bool``, *optional*):
            True, if this message is a forwarded copy of the original widget.

        can_send_queries (``bool``, *optional*):
            True, if the widget may send queries to the bot.

        can_send_background_queries (``bool``, *optional*):
            True, if the widget may send queries to the bot without user interaction.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        html: str,
        width: int = 0,
        height: int = 0,
        public_data: Optional[str] = None,
        chat_data: Optional[str] = None,
        id: Optional[int] = None,
        is_copy: Optional[bool] = None,
        can_send_queries: Optional[bool] = None,
        can_send_background_queries: Optional[bool] = None
    ):
        super().__init__(client)

        self.html = html
        self.width = width
        self.height = height
        self.public_data = public_data
        self.chat_data = chat_data
        self.id = id
        self.is_copy = is_copy
        self.can_send_queries = can_send_queries
        self.can_send_background_queries = can_send_background_queries

    @staticmethod
    def _parse(client, media: "raw.types.MessageMediaWidget") -> "Widget":
        # The server stores the HTML zlib-compressed (that is what its 4096-byte limit counts)
        try:
            html = zlib.decompress(media.payload)
        except zlib.error:  # tolerate a payload that is plain text
            html = media.payload

        return Widget(
            html=html.decode("utf-8", errors="replace"),
            width=media.width,
            height=media.height,
            public_data=media.public_data,
            chat_data=media.chat_data,
            id=media.widget_id,
            is_copy=media.is_copy or None,
            can_send_queries=media.can_query or None,
            can_send_background_queries=media.background_query or None,
            client=client
        )
