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


class GroupCall(Object):
    """Represents a group call.

    Parameters:
        id (``int``):
            Unique identifier of the group call.

        access_hash (``int``):
            Access hash for the group call.

        title (``str``, *optional*):
            Title of the group call.

        participants_count (``int``):
            Number of participants.

        version (``int``):
            Current version of the call state.

        stream_dc_id (``int``, *optional*):
            Data center ID for streaming.

        schedule_date (:py:obj:`~datetime.datetime`, *optional*):
            Scheduled start date.

        is_active (``bool``, *optional*):
            Whether the call is currently active.

        is_rtmp_stream (``bool``, *optional*):
            Whether this is an RTMP stream.

        is_listeners_hidden (``bool``, *optional*):
            Whether listener count is hidden.

        is_join_muted (``bool``, *optional*):
            Whether users join muted.

        is_can_change_join_muted (``bool``, *optional*):
            Whether join mute setting can be changed.

        is_video_started (``bool``, *optional*):
            Whether video has been started.

        is_can_start_video (``bool``, *optional*):
            Whether video can be started.

        is_record_started (``bool``, *optional*):
            Whether recording is active.

        record_video_active (``bool``, *optional*):
            Whether video recording is active.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int = None,
        access_hash: int = None,
        title: str = None,
        participants_count: int = None,
        version: int = None,
        stream_dc_id: int = None,
        schedule_date: datetime = None,
        is_active: bool = None,
        is_rtmp_stream: bool = None,
        is_listeners_hidden: bool = None,
        is_join_muted: bool = None,
        is_can_change_join_muted: bool = None,
        is_video_started: bool = None,
        is_can_start_video: bool = None,
        is_record_started: bool = None,
        record_video_active: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.access_hash = access_hash
        self.title = title
        self.participants_count = participants_count
        self.version = version
        self.stream_dc_id = stream_dc_id
        self.schedule_date = schedule_date
        self.is_active = is_active
        self.is_rtmp_stream = is_rtmp_stream
        self.is_listeners_hidden = is_listeners_hidden
        self.is_join_muted = is_join_muted
        self.is_can_change_join_muted = is_can_change_join_muted
        self.is_video_started = is_video_started
        self.is_can_start_video = is_can_start_video
        self.is_record_started = is_record_started
        self.record_video_active = record_video_active

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        call: "raw.types.GroupCall"
    ) -> "GroupCall":
        return GroupCall(
            client=client,
            id=call.id,
            access_hash=call.access_hash,
            title=call.title if hasattr(call, 'title') else None,
            participants_count=call.participants_count,
            version=call.version,
            stream_dc_id=call.stream_dc_id if hasattr(call, 'stream_dc_id') else None,
            schedule_date=utils.timestamp_to_datetime(call.schedule_date) if hasattr(call, 'schedule_date') and call.schedule_date else None,
            is_active=not call.schedule_date if hasattr(call, 'schedule_date') else True,
            is_rtmp_stream=call.rtmp_stream if hasattr(call, 'rtmp_stream') else None,
            is_listeners_hidden=call.listeners_hidden if hasattr(call, 'listeners_hidden') else None,
            is_join_muted=call.join_muted if hasattr(call, 'join_muted') else None,
            is_can_change_join_muted=call.can_change_join_muted if hasattr(call, 'can_change_join_muted') else None,
            is_video_started=call.video_started if hasattr(call, 'video_started') else None,
            is_can_start_video=call.can_start_video if hasattr(call, 'can_start_video') else None,
            is_record_started=call.record_started if hasattr(call, 'record_started') else None,
            record_video_active=call.record_video_active if hasattr(call, 'record_video_active') else None
        )
