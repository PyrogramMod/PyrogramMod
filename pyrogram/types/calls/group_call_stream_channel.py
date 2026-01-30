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

import pyrogram
from pyrogram import raw
from ..object import Object


class GroupCallStreamChannel(Object):
    """A group call stream channel.

    Parameters:
        channel (``int``):
            Channel identifier.

        scale (``int``):
            Channel scale.

        last_timestamp_ms (``int``):
            Last timestamp in milliseconds.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        channel: int,
        scale: int,
        last_timestamp_ms: int
    ):
        super().__init__(client)

        self.channel = channel
        self.scale = scale
        self.last_timestamp_ms = last_timestamp_ms

    @staticmethod
    def _parse(client: "pyrogram.Client", channel: "raw.types.GroupCallStreamChannel") -> "GroupCallStreamChannel":
        if not channel:
            return None

        return GroupCallStreamChannel(
            client=client,
            channel=channel.channel,
            scale=channel.scale,
            last_timestamp_ms=channel.last_timestamp_ms
        )
