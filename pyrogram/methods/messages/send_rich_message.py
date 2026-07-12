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

from datetime import datetime
from typing import Union, Optional

import pyrogram
from pyrogram import raw, types, utils


class SendRichMessage:
    async def send_rich_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        rich_message: "types.InputRichMessage",
        reply_to_message_id: Optional[int] = None,
        message_thread_id: Optional[int] = None,
        reply_markup: Optional["types.InlineKeyboardMarkup"] = None,
        schedule_date: Optional[datetime] = None,
        silent: Optional[bool] = None,
        protect_content: Optional[bool] = None,
    ) -> "types.Message":
        """Send a rich formatted message.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            rich_message (:obj:`~pyrogram.types.InputRichMessage`):
                Rich message content to send.

            reply_to_message_id (``int``, *optional*):
                Message ID to reply to.

            message_thread_id (``int``, *optional*):
                Forum topic ID for threaded messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                Inline keyboard markup.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            silent (``bool``, *optional*):
                Send silently (no notification).

            protect_content (``bool``, *optional*):
                Prevent message forwarding.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the sent message is returned.

        Example:
            .. code-block:: python

                from pyrogram.raw import types as raw_types
                from pyrogram.types import InputRichMessage

                await app.send_rich_message(
                    chat_id,
                    InputRichMessage(blocks=[
                        raw_types.PageBlockParagraph(
                            text=raw_types.TextPlain(text="Hello, rich world!")
                        )
                    ])
                )
        """
        reply_to = utils.get_reply_head_fm(message_thread_id, reply_to_message_id)

        r = await self.invoke(
            raw.functions.messages.SendMessage(
                peer=await self.resolve_peer(chat_id),
                message="",
                random_id=self.rnd_id(),
                rich_message=rich_message.write(),
                silent=silent or None,
                noforwards=protect_content or None,
                reply_to=reply_to,
                reply_markup=await reply_markup.write(self) if reply_markup else None,
                schedule_date=utils.datetime_to_timestamp(schedule_date),
            )
        )

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage, raw.types.UpdateNewChannelMessage,
                               raw.types.UpdateNewScheduledMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {u.id: u for u in r.users},
                    {c.id: c for c in r.chats}
                )
