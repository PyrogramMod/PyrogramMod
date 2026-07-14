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
from typing import Optional, List

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class ConferenceCall(Object):
    """Represents a conference call (1-on-1 video/voice call upgraded to group call).

    Parameters:
        id (``int``):
            Unique identifier of the conference call.

        access_hash (``int``):
            Access hash for the call.

        call (:obj:`~pyrogram.types.GroupCall`, *optional*):
            The underlying group call.

        participants (List of :obj:`~pyrogram.types.GroupCallParticipant`, *optional*):
            List of participants in the call.

        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            The chat associated with this conference.

        is_conference (``bool``, *optional*):
            Whether this is a conference call.

        is_can_invite (``bool``, *optional*):
            Whether you can invite more participants.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int = None,
        access_hash: int = None,
        call: "types.GroupCall" = None,
        participants: List["types.GroupCallParticipant"] = None,
        chat: "types.Chat" = None,
        is_conference: bool = None,
        is_can_invite: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.access_hash = access_hash
        self.call = call
        self.participants = participants
        self.chat = chat
        self.is_conference = is_conference
        self.is_can_invite = is_can_invite

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        call: "raw.types.phone.GroupCall",
        users: dict = None,
        chats: dict = None
    ) -> "ConferenceCall":
        users = users or {u.id: u for u in call.users} if hasattr(call, 'users') else {}
        chats = chats or {c.id: c for c in call.chats} if hasattr(call, 'chats') else {}

        group_call = None
        if hasattr(call, 'call') and call.call:
            group_call = types.GroupCall._parse(client, call.call)

        participants = []
        if hasattr(call, 'participants') and call.participants:
            for p in call.participants:
                participants.append(
                    types.GroupCallParticipant._parse(client, p, users, chats)
                )

        # Get associated chat
        chat = None
        if hasattr(call, 'call') and call.call and hasattr(call.call, 'id'):
            for chat_raw in chats.values():
                if hasattr(chat_raw, 'call') and chat_raw.call:
                    if chat_raw.call.id == call.call.id:
                        if hasattr(chat_raw, 'broadcast') and chat_raw.broadcast:
                            chat = types.Chat._parse_channel_chat(client, chat_raw)
                        elif hasattr(chat_raw, 'megagroup') and chat_raw.megagroup:
                            chat = types.Chat._parse_channel_chat(client, chat_raw)
                        break

        return ConferenceCall(
            client=client,
            id=call.call.id if hasattr(call, 'call') and call.call else None,
            access_hash=call.call.access_hash if hasattr(call, 'call') and call.call else None,
            call=group_call,
            participants=types.List(participants) if participants else None,
            chat=chat,
            is_conference=True,
            is_can_invite=True
        )
