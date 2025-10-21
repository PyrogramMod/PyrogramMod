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

import asyncio
from typing import List
from typing import Optional
from typing import Sequence
from typing import Union

import pyrogram
from pyrogram import enums
from pyrogram import raw
from pyrogram import types
from pyrogram import utils


class SendStreamingText:
    async def send_streaming_text(
            self: "pyrogram.Client",
            chat_id: Union[int, str],
            streaming_text: Union[str, Sequence[str]],
            delay: float = 2.0,
            parse_mode: Optional["enums.ParseMode"] = None,
            entities: Optional[List["types.MessageEntity"]] = None,
            reply_to_message_id: Optional[int] = None,
            message_thread_id: Optional[int] = None,
    ) -> bool:
        """Send a sequence of live *thinking/streaming text*.

        .. include:: /_includes/usable-by/bots.rst

        Telegram clients display the native **“Thinking…”** status while these updates are streamed,
        just like the official AI bot experience.

        This method uses the low-level
        :obj:`~pyrogram.raw.functions.messages.SetTyping` method with
        :obj:`~pyrogram.raw.types.SendMessageTextDraftAction` to send
        **thinking / streaming text generation** updates to the recipient.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            streaming_text (``str`` | Sequence of ``str``):
                Text or text chunks to send as streaming “thinking” updates.
                When a single string is passed, it is sent as one update.

            delay (``float``, *optional*):
                Delay (in seconds) between successive streaming updates. Defaults to 2.0.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                Mode for parsing entities if they are used inside the streaming text (rare).

            entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                Special entities that appear in the streaming text entries.

            reply_to_message_id (``int``, *optional*):
                ID of the original message to reply to.

            message_thread_id (``int``, *optional*):
                Forum topic ID. Required for threaded replies in forum chats.

        Returns:
            ``bool``: The result of the last streamed typing update.

        Example:
            .. code-block:: python

                # Send a thinking stream
                await app.send_streaming_text(
                    message.chat.id,
                    streaming_text=[
                        "Hello! Let me think…",
                        "OK, I see what you need…",
                        "Working out the details…",
                        "Here comes the final advice…"
                    ],
                    message_thread_id=message.message_thread_id,
                    delay=2.0
                )

                # Single chunk variant
                await app.send_streaming_text(
                    message.chat.id,
                    streaming_text="Hello! Let me think…",
                    message_thread_id=message.message_thread_id
                )
        """

        if isinstance(streaming_text, str):
            chunks = [streaming_text]
        else:
            chunks = list(streaming_text)

        if not chunks:
            return False

        should_parse_entities = bool(parse_mode or entities)
        parsed_chunks = []

        for chunk in chunks:
            if not isinstance(chunk, str):
                raise TypeError("Each streaming_text entry must be a string.")

            if should_parse_entities:
                parsed = await utils.parse_text_entities(
                    self,
                    chunk,
                    parse_mode,
                    entities
                )

                message_text = parsed["message"]
                message_entities = parsed["entities"] or []
            else:
                message_text = chunk
                message_entities = []

            parsed_chunks.append((message_text, message_entities))

        peer = await self.resolve_peer(chat_id)
        reply_to = utils.get_reply_head_fm(message_thread_id, reply_to_message_id)
        top_msg_id = reply_to.top_msg_id if reply_to else message_thread_id
        typing_random_id = self.rnd_id()

        result = False
        total_chunks = len(parsed_chunks)

        for idx, (text, text_entities) in enumerate(parsed_chunks, start=1):
            result = await self.invoke(
                raw.functions.messages.SetTyping(
                    peer=peer,
                    action=raw.types.SendMessageTextDraftAction(
                        random_id=typing_random_id,
                        text=raw.types.TextWithEntities(
                            text=text,
                            entities=text_entities
                        )
                    ),
                    top_msg_id=top_msg_id
                )
            )

            if idx != total_chunks and delay and delay > 0:
                await asyncio.sleep(delay)

        return result
