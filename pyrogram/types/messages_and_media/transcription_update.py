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

from typing import Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object
from ..update import Update


class TranscriptionUpdate(Object, Update):
    """A transcription changed, usually its text became final.

    Parameters:
        id (``int``):
            Identifier of the transcription.

        text (``str``):
            Transcribed text.

        is_pending (``bool``):
            True, if the transcription is still not final.

        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Chat of the transcribed message. None for transcriptions of an uploaded file.

        message_id (``int``, *optional*):
            Identifier of the transcribed message. None for transcriptions of an uploaded file.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        text: str,
        is_pending: bool = False,
        chat: "types.Chat" = None,
        message_id: Optional[int] = None
    ):
        super().__init__(client)

        self.id = id
        self.text = text
        self.is_pending = is_pending
        self.chat = chat
        self.message_id = message_id

    @staticmethod
    def _parse(client, update, users, chats) -> "TranscriptionUpdate":
        in_chat = isinstance(update, raw.types.UpdateTranscribedAudio)

        return TranscriptionUpdate(
            id=update.transcription_id,
            text=update.text,
            is_pending=bool(update.pending),
            chat=utils.parse_peer_chat(client, update.peer, users, chats) if in_chat else None,
            message_id=update.msg_id if in_chat else None,
            client=client
        )
