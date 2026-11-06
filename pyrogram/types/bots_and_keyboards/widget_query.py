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

from typing import Optional, Union

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object
from ..update import Update


class WidgetQuery(Object, Update):
    """An incoming query sent by a widget to its bot.

    Every query must be answered with :meth:`~pyrogram.Client.answer_widget_query` (also when something failed):
    an unanswered query ends in the widget as ``TIMEOUT`` after 15 seconds.

    Parameters:
        id (``str``):
            Unique identifier of the query.

        from_user (:obj:`~pyrogram.types.User`):
            The user who made the query.

        data (``str`` | ``bytes``):
            Data sent by the widget (1-64 bytes).

        type (``str``):
            ``"data"``, ``"sign_data"`` or ``"sent_transaction"``.

        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Chat of the widget message. Only for queries from an original widget message.

        message_id (``int``, *optional*):
            Identifier of the widget message in *chat*.

        inline_message_id (``str``, *optional*):
            Identifier of the widget message sent via the bot in inline mode.

        chat_instance (``str``, *optional*):
            Global identifier of the chat the widget message is in.

        chat_type (``str``, *optional*):
            ``"private"``, ``"group"``, ``"supergroup"`` or ``"channel"``.

        widget_id (``int``, *optional*):
            Identifier of the shared widget, if the widget is shared.

        is_copy (``bool``):
            True, if the query comes from a forwarded copy of a shared widget (``shared_widget_query``).
            Such a query has no *chat*, *message_id* or *inline_message_id*.

        sign_data (``str``, *optional*):
            Data to sign. Only when *type* is ``"sign_data"``.

        msg_hash (``str``, *optional*):
            Hash of the sent transaction. Only when *type* is ``"sent_transaction"``.

        wallet (:obj:`~pyrogram.raw.base.UserWallet`, *optional*):
            Raw wallet of the user, for ``"sign_data"`` and ``"sent_transaction"``.

        wallet_card (:obj:`~pyrogram.raw.base.wallet.Card`, *optional*):
            Raw wallet card, if sent.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        from_user: "types.User",
        data: Union[str, bytes],
        type: str = "data",
        chat: "types.Chat" = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        chat_instance: Optional[str] = None,
        chat_type: Optional[str] = None,
        widget_id: Optional[int] = None,
        is_copy: bool = False,
        sign_data: Optional[str] = None,
        msg_hash: Optional[str] = None,
        wallet: "raw.base.UserWallet" = None,
        wallet_card: "raw.base.wallet.Card" = None
    ):
        super().__init__(client)

        self.id = id
        self.from_user = from_user
        self.data = data
        self.type = type
        self.chat = chat
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.chat_type = chat_type
        self.widget_id = widget_id
        self.is_copy = is_copy
        self.sign_data = sign_data
        self.msg_hash = msg_hash
        self.wallet = wallet
        self.wallet_card = wallet_card

    @staticmethod
    def _parse(client: "pyrogram.Client", update, users, chats) -> "WidgetQuery":
        # Like callback queries: a non-UTF-8 payload falls back to bytes.
        try:
            data = update.data.decode()
        except (UnicodeDecodeError, AttributeError):
            data = update.data

        query_type = "data"
        sign_data = msg_hash = wallet = None
        qt = update.query_type

        if isinstance(qt, raw.types.WidgetQueryTypeSignData):
            query_type, sign_data, wallet = "sign_data", qt.sign_data.data, qt.wallet
        elif isinstance(qt, raw.types.WidgetQueryTypeSentTransaction):
            query_type, msg_hash, wallet = "sent_transaction", qt.msg_hash, qt.wallet

        chat = message_id = inline_message_id = None

        if isinstance(update, raw.types.UpdateBotWidgetQuery):
            chat_id = utils.get_peer_id(update.peer)
            raw_chat = users.get(chat_id) if chat_id > 0 else chats.get(utils.get_raw_peer_id(update.peer))
            chat = types.Chat._parse_chat(client, raw_chat) if raw_chat else None
            message_id = update.msg_id
        elif isinstance(update, raw.types.UpdateInlineBotWidgetQuery):
            inline_message_id = utils.pack_inline_message_id(update.inline_message_id)

        is_copy = isinstance(update, raw.types.UpdateBotWidgetCopyQuery)

        return WidgetQuery(
            id=str(update.query_id),
            from_user=types.User._parse(client, users[update.user_id]),
            data=data,
            type=query_type,
            chat=chat,
            message_id=message_id,
            inline_message_id=inline_message_id,
            chat_instance=None if is_copy else str(update.chat_instance),
            chat_type=None if is_copy else update.chat_type,
            widget_id=update.widget_id,
            is_copy=is_copy,
            sign_data=sign_data,
            msg_hash=msg_hash,
            wallet=wallet,
            wallet_card=getattr(update, "wallet_card", None),
            client=client
        )

    async def answer(self, data: str = "") -> bool:
        """Bound method *answer* of :obj:`~pyrogram.types.WidgetQuery`.

        Use as a shortcut for:

        .. code-block:: python

            await client.answer_widget_query(widget_query.id, data)

        Parameters:
            data (``str``, *optional*):
                Answer sent to the widget, at most 1024 bytes.

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self._client.answer_widget_query(self.id, data)
