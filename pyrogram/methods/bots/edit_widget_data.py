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

from typing import Union, Optional

import pyrogram
from pyrogram import raw, utils
from pyrogram.methods.messages.inline_session import get_session


class EditWidgetData:
    async def edit_message_widget_data(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        public_data: Optional[str] = None,
        chat_data: Optional[str] = None
    ) -> bool:
        """Change the state of a widget message (Bot API 10.4 ``editMessageWidgetData``).

        An edit that changes nothing fails with ``MESSAGE_NOT_MODIFIED``: take it as done.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the widget message.

            public_data (``str``, *optional*):
                New shared state of this message, at most 1024 bytes.

            chat_data (``str``, *optional*):
                New state of this message only, at most 1024 bytes.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.edit_message_widget_data(chat_id, message_id, chat_data="turn:2")
        """
        await self.invoke(
            raw.functions.messages.EditMessageWidgetData(
                peer=await self.resolve_peer(chat_id),
                id=message_id,
                public_data=public_data,
                chat_data=chat_data
            )
        )

        return True

    async def edit_inline_widget_data(
        self: "pyrogram.Client",
        inline_message_id: str,
        public_data: Optional[str] = None,
        chat_data: Optional[str] = None
    ) -> bool:
        """Change the state of an inline widget message (Bot API 10.4 ``editMessageWidgetData`` with ``inline_message_id``).

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            inline_message_id (``str``):
                Identifier of the inline message.

            public_data (``str``, *optional*):
                New shared state, at most 1024 bytes.

            chat_data (``str``, *optional*):
                New state of this message only, at most 1024 bytes.

        Returns:
            ``bool``: On success, True is returned.
        """
        unpacked = utils.unpack_inline_message_id(inline_message_id)
        session = await get_session(self, unpacked.dc_id)

        return await session.invoke(
            raw.functions.messages.EditInlineBotMessageWidgetData(
                id=unpacked,
                public_data=public_data,
                chat_data=chat_data
            ),
            sleep_threshold=self.sleep_threshold
        )

    async def edit_shared_widget_data(
        self: "pyrogram.Client",
        widget_id: int,
        public_data: str,
        cache_time: Optional[int] = None
    ) -> bool:
        """Change the state of a shared widget everywhere (Bot API 10.4 ``editSharedWidgetData``).

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            widget_id (``int``):
                Identifier of the shared widget (:attr:`~pyrogram.types.Widget.id`).

            public_data (``str``):
                New shared state, at most 1024 bytes.

            cache_time (``int``, *optional*):
                Poll period of the clients in seconds, 5-3600.

        Returns:
            ``bool``: On success, True is returned.
        """
        return await self.invoke(
            raw.functions.messages.EditWidgetData(
                widget_id=widget_id,
                public_data=public_data,
                cache_time=cache_time
            )
        )
