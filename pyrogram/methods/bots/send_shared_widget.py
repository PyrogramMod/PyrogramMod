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

from typing import Union, List, Optional

import pyrogram
from pyrogram import raw, types, enums
from .send_widget import _send_widget_media


class SendSharedWidget:
    async def send_shared_widget(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        widget_id: int,
        chat_data: Optional[str] = None,
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        invert_media: bool = None,
        disable_notification: bool = None,
        reply_to_message_id: int = None,
        message_thread_id: int = None,
        protect_content: bool = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None
    ) -> "types.Message":
        """Post an existing shared widget again (Bot API 10.4 ``sendSharedWidget``).

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            widget_id (``int``):
                Identifier of the shared widget (:attr:`~pyrogram.types.Widget.id`). Must be one of this bot's.

            chat_data (``str``, *optional*):
                State of this message only, at most 1024 bytes.

            caption (``str``, *optional*):
                Widget caption.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                Parse mode of *caption*.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                Entities of *caption*, which can be specified instead of *parse_mode*.

            invert_media (``bool``, *optional*):
                Show the caption above the widget.

            disable_notification (``bool``, *optional*):
                Sends the message silently.

            reply_to_message_id (``int``, *optional*):
                If the message is a reply, ID of the original message.

            message_thread_id (``int``, *optional*):
                If the message is in a thread, ID of the original message.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                Inline keyboard under the widget.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent widget message is returned.

        Example:
            .. code-block:: python

                await app.send_shared_widget(chat_id, widget_id)
        """
        return await _send_widget_media(
            self, chat_id,
            raw.types.InputMediaWidgetId(widget_id=widget_id, chat_data=chat_data),
            caption, parse_mode, caption_entities, invert_media,
            disable_notification, reply_to_message_id, message_thread_id, protect_content, reply_markup
        )
