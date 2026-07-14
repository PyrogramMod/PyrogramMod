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
from pyrogram import raw, types, utils


class SendRichMessageDraft:
    async def send_rich_message_draft(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        rich_message: "types.InputRichMessage",
        message_thread_id: Optional[int] = None,
        reply_to_message_id: Optional[int] = None,
    ) -> bool:
        """Stream a partial rich message as a typing indicator.

        Sends a ``SetTyping`` action with
        ``InputSendMessageRichMessageDraftAction`` so clients display the
        message being composed in real time.  Call repeatedly with updated
        content to stream progressively-generated rich replies.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Target chat.

            rich_message (:obj:`~pyrogram.types.InputRichMessage`):
                Partial rich message content.

            message_thread_id (``int``, *optional*):
                Forum topic ID.

            reply_to_message_id (``int``, *optional*):
                Message being replied to.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                from pyrogram.raw import types as raw_types
                from pyrogram.types import InputRichMessage

                await app.send_rich_message_draft(
                    chat_id,
                    InputRichMessage(blocks=[
                        raw_types.PageBlockParagraph(
                            text=raw_types.TextPlain(text="Generating…")
                        )
                    ])
                )
        """
        peer = await self.resolve_peer(chat_id)
        reply_to = utils.get_reply_head_fm(message_thread_id, reply_to_message_id)
        top_msg_id = reply_to.top_msg_id if reply_to else message_thread_id

        return await self.invoke(
            raw.functions.messages.SetTyping(
                peer=peer,
                action=raw.types.InputSendMessageRichMessageDraftAction(
                    random_id=self.rnd_id(),
                    rich_message=rich_message.write(),
                ),
                top_msg_id=top_msg_id,
            )
        )
