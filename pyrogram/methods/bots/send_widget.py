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
from pyrogram import raw, utils, types, enums


async def _send_widget_media(
    client: "pyrogram.Client",
    chat_id: Union[int, str],
    media: "raw.base.InputMedia",
    caption: str,
    parse_mode: Optional["enums.ParseMode"],
    caption_entities: List["types.MessageEntity"],
    invert_media: Optional[bool],
    disable_notification: Optional[bool],
    reply_to_message_id: Optional[int],
    message_thread_id: Optional[int],
    protect_content: Optional[bool],
    reply_markup
) -> "types.Message":
    message, entities = (await utils.parse_text_entities(
        client, caption, parse_mode, caption_entities
    )).values()

    r = await client.invoke(
        raw.functions.messages.SendMedia(
            peer=await client.resolve_peer(chat_id),
            media=media,
            message=message,
            entities=entities,
            invert_media=invert_media or None,
            silent=disable_notification or None,
            reply_to=utils.get_reply_head_fm(message_thread_id, reply_to_message_id),
            random_id=client.rnd_id(),
            noforwards=protect_content,
            reply_markup=await reply_markup.write(client) if reply_markup else None
        )
    )

    for i in r.updates:
        if isinstance(i, (raw.types.UpdateNewMessage, raw.types.UpdateNewChannelMessage)):
            return await types.Message._parse(
                client, i.message,
                {i.id: i for i in r.users},
                {i.id: i for i in r.chats}
            )


class SendWidget:
    async def send_widget(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        html: str,
        width: int = 0,
        height: int = 0,
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        chat_data: Optional[str] = None,
        public_data: Optional[str] = None,
        allow_queries: bool = None,
        is_shared: bool = None,
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
        """Send a widget (Bot API 10.4 ``sendWidget``).

        A widget is a self-contained HTML document drawn inside the message bubble.
        The server refuses HTML over 32768 bytes, or over 4096 bytes once zlib-compressed
        (``INPUT_MEDIA_WIDGET_TOO_LARGE``).

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            html (``str``):
                The widget's HTML document.

            width (``int``, *optional*):
                Width size anchor, 0 means auto.

            height (``int``, *optional*):
                Height size anchor, 0 means auto.

            caption (``str``, *optional*):
                Widget caption, shown in previews, the chat list and search.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                Parse mode of *caption*.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                Entities of *caption*, which can be specified instead of *parse_mode*.

            chat_data (``str``, *optional*):
                State of this message only, at most 1024 bytes.

            public_data (``str``, *optional*):
                State shared by every copy of a shared widget, at most 1024 bytes.

            allow_queries (``bool``, *optional*):
                Let the widget send queries to the bot (:obj:`~pyrogram.types.WidgetQuery`).
                In the private chat with the bot the widget may also query in the background.

            is_shared (``bool``, *optional*):
                One shared state for every copy. The sent widget has an :attr:`~pyrogram.types.Widget.id`;
                together with *allow_queries* its forwards may send queries too.

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

                await app.send_widget(chat_id, "<button>Hi</button>", allow_queries=True)
        """
        return await _send_widget_media(
            self, chat_id,
            raw.types.InputMediaWidget(
                allow_queries=allow_queries or None,
                shared_widget=is_shared or None,
                width=width or 0,
                height=height or 0,
                html=html,
                public_data=public_data,
                chat_data=chat_data
            ),
            caption, parse_mode, caption_entities, invert_media,
            disable_notification, reply_to_message_id, message_thread_id, protect_content, reply_markup
        )
