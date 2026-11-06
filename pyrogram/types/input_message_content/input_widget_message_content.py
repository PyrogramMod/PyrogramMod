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

from typing import Optional, List

import pyrogram
from pyrogram import raw, types, utils, enums
from .input_message_content import InputMessageContent


class InputWidgetMessageContent(InputMessageContent):
    """Content of a widget message to be sent as the result of an inline query.

    Parameters:
        html (``str``):
            The widget's HTML document (at most 4096 bytes once zlib-compressed).

        width (``int``, *optional*):
            Width size anchor, 0 or None means auto.

        height (``int``, *optional*):
            Height size anchor, 0 or None means auto.

        caption (``str``, *optional*):
            Caption shown in previews, the chat list and search.

        parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
            Parse mode of *caption*.

        caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Entities of *caption*, which can be specified instead of *parse_mode*.

        chat_data (``str``, *optional*):
            State of this message, at most 1024 bytes.

        public_data (``str``, *optional*):
            State shared by every copy of a shared widget, at most 1024 bytes.

        allow_queries (``bool``, *optional*):
            Pass True to let the widget send queries to the bot.

        is_shared (``bool``, *optional*):
            Pass True to make the widget shared: one state for every copy.

        invert_media (``bool``, *optional*):
            Pass True to show the caption above the widget.
    """

    def __init__(
        self,
        html: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        chat_data: Optional[str] = None,
        public_data: Optional[str] = None,
        allow_queries: bool = None,
        is_shared: bool = None,
        invert_media: bool = None
    ):
        super().__init__()

        self.html = html
        self.width = width
        self.height = height
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.chat_data = chat_data
        self.public_data = public_data
        self.allow_queries = allow_queries
        self.is_shared = is_shared
        self.invert_media = invert_media

    async def write(self, client: "pyrogram.Client", reply_markup):
        message, entities = (await utils.parse_text_entities(
            client, self.caption, self.parse_mode, self.caption_entities
        )).values()

        return raw.types.InputBotInlineMessageWidget(
            allow_queries=self.allow_queries or None,
            shared_widget=self.is_shared or None,
            invert_media=self.invert_media or None,
            width=self.width or 0,
            height=self.height or 0,
            html=self.html,
            public_data=self.public_data,
            chat_data=self.chat_data,
            reply_markup=await reply_markup.write(client) if reply_markup else None,
            message=message,
            entities=entities
        )
