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
from typing import Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class GroupCallParticipant(Object):
    """Represents a participant in a group call.

    Parameters:
        user (:obj:`~pyrogram.types.User`, *optional*):
            The participant user.

        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            The participant chat (if joined as channel).

        date (:py:obj:`~datetime.datetime`):
            When the participant joined.

        source (``int``):
            Audio source identifier.

        volume (``int``, *optional*):
            Participant volume (0-20000).

        is_muted (``bool``, *optional*):
            Whether the participant is muted.

        is_muted_by_you (``bool``, *optional*):
            Whether muted by current user.

        is_can_self_unmute (``bool``, *optional*):
            Whether can self-unmute.

        is_left (``bool``, *optional*):
            Whether has left the call.

        is_just_joined (``bool``, *optional*):
            Whether just joined.

        is_versioned (``bool``, *optional*):
            Whether participant state is versioned.

        is_video (``bool``, *optional*):
            Whether video is enabled.

        is_screen (``bool``, *optional*):
            Whether screen sharing is enabled.

        raise_hand_rating (``int``, *optional*):
            Hand raise rating for ordering.

        video_timestamp (``int``, *optional*):
            Video stream timestamp.

        presentation_timestamp (``int``, *optional*):
            Presentation stream timestamp.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        user: "types.User" = None,
        chat: "types.Chat" = None,
        date: datetime = None,
        source: int = None,
        volume: int = None,
        is_muted: bool = None,
        is_muted_by_you: bool = None,
        is_can_self_unmute: bool = None,
        is_left: bool = None,
        is_just_joined: bool = None,
        is_versioned: bool = None,
        is_video: bool = None,
        is_screen: bool = None,
        raise_hand_rating: int = None,
        video_timestamp: int = None,
        presentation_timestamp: int = None
    ):
        super().__init__(client)

        self.user = user
        self.chat = chat
        self.date = date
        self.source = source
        self.volume = volume
        self.is_muted = is_muted
        self.is_muted_by_you = is_muted_by_you
        self.is_can_self_unmute = is_can_self_unmute
        self.is_left = is_left
        self.is_just_joined = is_just_joined
        self.is_versioned = is_versioned
        self.is_video = is_video
        self.is_screen = is_screen
        self.raise_hand_rating = raise_hand_rating
        self.video_timestamp = video_timestamp
        self.presentation_timestamp = presentation_timestamp

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        participant: "raw.types.GroupCallParticipant",
        users: dict,
        chats: dict
    ) -> "GroupCallParticipant":
        user = None
        chat = None

        peer = participant.peer
        if isinstance(peer, raw.types.PeerUser):
            if peer.user_id in users:
                user = types.User._parse(client, users[peer.user_id])
        elif isinstance(peer, raw.types.PeerChannel):
            if peer.channel_id in chats:
                chat = types.Chat._parse_channel_chat(client, chats[peer.channel_id])
        elif isinstance(peer, raw.types.PeerChat):
            if peer.chat_id in chats:
                chat = types.Chat._parse_chat_chat(client, chats[peer.chat_id])

        return GroupCallParticipant(
            client=client,
            user=user,
            chat=chat,
            date=utils.timestamp_to_datetime(participant.date),
            source=participant.source,
            volume=participant.volume if hasattr(participant, 'volume') else None,
            is_muted=participant.muted if hasattr(participant, 'muted') else None,
            is_muted_by_you=participant.muted_by_you if hasattr(participant, 'muted_by_you') else None,
            is_can_self_unmute=participant.can_self_unmute if hasattr(participant, 'can_self_unmute') else None,
            is_left=participant.left if hasattr(participant, 'left') else None,
            is_just_joined=participant.just_joined if hasattr(participant, 'just_joined') else None,
            is_versioned=participant.versioned if hasattr(participant, 'versioned') else None,
            is_video=bool(participant.video) if hasattr(participant, 'video') else None,
            is_screen=bool(participant.presentation) if hasattr(participant, 'presentation') else None,
            raise_hand_rating=participant.raise_hand_rating if hasattr(participant, 'raise_hand_rating') else None,
            video_timestamp=participant.video.audio_timestamp if hasattr(participant, 'video') and participant.video and hasattr(participant.video, 'audio_timestamp') else None,
            presentation_timestamp=participant.presentation.audio_timestamp if hasattr(participant, 'presentation') and participant.presentation and hasattr(participant.presentation, 'audio_timestamp') else None
        )
