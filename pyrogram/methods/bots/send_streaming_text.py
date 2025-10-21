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
from datetime import datetime
from typing import List, Optional, Tuple, Union

import pyrogram
from pyrogram import enums
from pyrogram import raw
from pyrogram import types
from pyrogram import utils


class SendStreamingText:
    async def send_streaming_text(
            self: "pyrogram.Client",
            chat_id: Union[int, str],
            streaming_text: List[str],
            delay: float = 2.0,
            final_delay: Optional[float] = None,
            parse_mode: Optional["enums.ParseMode"] = None,
            entities: Optional[List["types.MessageEntity"]] = None,
            disable_web_page_preview: Optional[bool] = None,
            disable_notification: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            message_thread_id: Optional[int] = None,
            schedule_date: Optional[datetime] = None,
            protect_content: Optional[bool] = None,
            reply_markup: Optional[Union[
                "types.InlineKeyboardMarkup",
                "types.ReplyKeyboardMarkup",
                "types.ReplyKeyboardRemove",
                "types.ForceReply"
            ]] = None,
            final_text: Optional[str] = None
    ) -> Union[bool, Tuple["types.Message", bool]]:
        """Send a sequence of live *thinking/streaming text* updates before a final message.

        .. include:: /_includes/usable-by/bots.rst

        This method uses the low-level
        :obj:`~pyrogram.raw.functions.messages.SetTyping` method with
        :obj:`~pyrogram.raw.types.SendMessageTextDraftAction` to send
        **thinking / streaming text generation** updates to the recipient.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            streaming_text (List of ``str``):
                Text chunks to send as streaming “thinking” updates.

            delay (``float``, *optional*):
                Delay (in seconds) between successive streaming updates. Defaults to 2.0.

            final_delay (``float``, *optional*):
                Pause (in seconds) after cancelling the typing indicator and before sending *final_text*.
                Defaults to the same value as *delay*.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                Mode for parsing entities in *final_text*, if provided.

            entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                Special entities that appear in *final_text*.

            disable_web_page_preview (``bool``, *optional*):
                Disables link previews for links in *final_text*.

            disable_notification (``bool``, *optional*):
                Sends the *final_text* message silently.

            reply_to_message_id (``int``, *optional*):
                ID of the original message to reply to.

            message_thread_id (``int``, *optional*):
                Forum topic ID. Required for threaded replies in forum chats.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the *final_text* will be automatically sent.

            protect_content (``bool``, *optional*):
                Protects the contents of the *final_text* message from forwarding and saving.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options for the final message.

            final_text (``str``, *optional*):
                The final message to send after the streaming sequence.
                If omitted, only the thinking stream will be sent.

        Returns:
            ( :obj:`~pyrogram.types.Message`, ``bool`` ) | ``bool``:
                If *final_text* is provided, returns a tuple with the sent message and the result of the last typing action.
                Otherwise, returns the boolean result of the cancel typing action.

        Example:
            .. code-block:: python

                # Send thinking stream followed by final message
                await app.send_streaming_text(
                    "me",
                    streaming_text=["Thinking...", "Composing reply...", "Finalizing..."],
                    delay=2.0,
                    final_text="✅ Done!"
                )
        """

        peer = await self.resolve_peer(chat_id)
        reply_to = utils.get_reply_head_fm(message_thread_id, reply_to_message_id)

        rt = False

        if streaming_text:
            typing_random_id = self.rnd_id()
            total_chunks = len(streaming_text)

            for idx, text in enumerate(streaming_text, start=1):
                rt = await self.invoke(
                    raw.functions.messages.SetTyping(
                        peer=peer,
                        action=raw.types.SendMessageTextDraftAction(
                            random_id=typing_random_id,
                            text=raw.types.TextWithEntities(
                                text=text,
                                entities=[]
                            )
                        ),
                        top_msg_id=reply_to.top_msg_id if reply_to else message_thread_id
                    )
                )

                if idx != total_chunks and delay:
                    await asyncio.sleep(delay)

            rt = await self.invoke(
                raw.functions.messages.SetTyping(
                    peer=peer,
                    action=raw.types.SendMessageCancelAction(),
                    top_msg_id=reply_to.top_msg_id if reply_to else message_thread_id
                )
            )

        if not final_text:
            return rt

        final_delay_value = delay if final_delay is None else final_delay
        if streaming_text and final_delay_value:
            await asyncio.sleep(final_delay_value)

        message, entities = (await utils.parse_text_entities(self, final_text, parse_mode, entities)).values()
        raw_reply_markup = await reply_markup.write(self) if reply_markup else None

        r = await self.invoke(
            raw.functions.messages.SendMessage(
                peer=peer,
                no_webpage=disable_web_page_preview or None,
                silent=disable_notification or None,
                reply_to=reply_to,
                random_id=self.rnd_id(),
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                reply_markup=raw_reply_markup,
                message=message,
                entities=entities,
                noforwards=protect_content
            )
        )

        if isinstance(r, raw.types.UpdateShortSentMessage):
            peer_id = (
                peer.user_id
                if isinstance(peer, raw.types.InputPeerUser)
                else -peer.chat_id
            )

            message_obj = types.Message(
                id=r.id,
                chat=types.Chat(
                    id=peer_id,
                    type=enums.ChatType.PRIVATE,
                    client=self
                ),
                text=message,
                date=utils.timestamp_to_datetime(r.date),
                outgoing=r.out,
                reply_markup=reply_markup,
                reply_to_message_id=reply_to_message_id,
                reply_to_top_message_id=message_thread_id,
                message_thread_id=message_thread_id,
                entities=[
                    types.MessageEntity._parse(None, entity, {})
                    for entity in entities
                ] if entities else None,
                client=self
            )

            return message_obj, rt

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                              raw.types.UpdateNewChannelMessage,
                              raw.types.UpdateNewScheduledMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats},
                    is_scheduled=isinstance(i, raw.types.UpdateNewScheduledMessage)
                ), rt
