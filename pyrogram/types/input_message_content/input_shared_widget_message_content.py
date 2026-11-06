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


class InputSharedWidgetMessageContent(InputMessageContent):
    """Content of a message with an already existing shared widget, to be sent as the result of an inline query.

    Parameters:
        widget_id (``int``):
            Identifier of the shared widget (:attr:`~pyrogram.types.Widget.id`).

        chat_data (``str``, *optional*):
            State of this message, at most 1024 bytes.

        caption (``str``, *optional*):
            Caption shown in previews, the chat list and search.

        parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
            Parse mode of *caption*.

        caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Entities of *caption*, which can be specified instead of *parse_mode*.

        invert_media (``bool``, *optional*):
            Pass True to show the caption above the widget.
    """

    def __init__(
        self,
        widget_id: int,
        chat_data: Optional[str] = None,
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        invert_media: bool = None
    ):
        super().__init__()

        self.widget_id = widget_id
        self.chat_data = chat_data
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.invert_media = invert_media

    async def write(self, client: "pyrogram.Client", reply_markup):
        message, entities = (await utils.parse_text_entities(
            client, self.caption, self.parse_mode, self.caption_entities
        )).values()

        return raw.types.InputBotInlineMessageWidgetId(
            invert_media=self.invert_media or None,
            widget_id=self.widget_id,
            chat_data=self.chat_data,
            reply_markup=await reply_markup.write(client) if reply_markup else None,
            message=message,
            entities=entities
        )
