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

from typing import Union, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class EditEphemeralMessage:
    async def edit_ephemeral_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str],
        message_id: int,
        text: Optional[str] = None,
        media: Optional["raw.base.InputMedia"] = None,
        entities: Optional["raw.base.MessageEntity"] = None,
        reply_markup: Optional["raw.base.ReplyMarkup"] = None,
        rich_message: Optional["raw.base.InputRichMessage"] = None,
        invert_media: bool = False,
        welcome: bool = False,
    ) -> Optional["types.Message"]:
        """Edit an ephemeral message previously sent with :meth:`~pyrogram.Client.send_ephemeral_message`.

        Ephemeral messages are visible only to a specific user within a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the user that will receive the ephemeral message.

            message_id (``int``):
                Identifier of the ephemeral message to edit.

            text (``str``, *optional*):
                New text of the message.

            media (:obj:`~pyrogram.raw.base.InputMedia`, *optional*):
                New media content.

            entities (:obj:`~pyrogram.raw.base.MessageEntity`, *optional*):
                New message entities.

            reply_markup (:obj:`~pyrogram.raw.base.ReplyMarkup`, *optional*):
                New reply markup.

            rich_message (:obj:`~pyrogram.raw.base.InputRichMessage`, *optional*):
                New rich message content.

            invert_media (``bool``, *optional*):
                Pass True to invert media position.

            welcome (``bool``, *optional*):
                Pass True if this is a welcome message.

        Returns:
            :obj:`~pyrogram.types.Message` | ``None``: On success, the edited message is returned,
            otherwise None.

        Example:
            .. code-block:: python

                await app.edit_ephemeral_message(
                    chat_id, user_id, message_id,
                    text="Updated text"
                )
        """
        peer = await self.resolve_peer(chat_id)
        receiver = await self.resolve_peer(user_id)

        r = await self.invoke(
            raw.functions.ephemeral.EditMessage(
                peer=peer,
                receiver_id=receiver,
                id=message_id,
                message=text,
                media=media,
                entities=entities,
                reply_markup=reply_markup,
                rich_message=rich_message,
                invert_media=invert_media or None,
                welcome=welcome or None,
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                              raw.types.UpdateNewChannelMessage,
                              raw.types.UpdateEditMessage,
                              raw.types.UpdateEditChannelMessage)):
                return await types.Message._parse(
                    self, i.message, users, chats
                )

        return None
