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
from pyrogram import raw, utils
from ..object import Object


class StoriesStealthMode(Object):
    """Information about the stealth mode for stories.

    When stealth mode is enabled, the user's views of other users' stories
    will not be recorded for a period of time.

    Parameters:
        active_until (:py:obj:`~datetime.datetime`, *optional*):
            If set, stealth mode is currently active and will be until this date.

        cooldown_until (:py:obj:`~datetime.datetime`, *optional*):
            If set, the user can't enable stealth mode again until this date.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        active_until: datetime = None,
        cooldown_until: datetime = None
    ):
        super().__init__(client)

        self.active_until = active_until
        self.cooldown_until = cooldown_until

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        stealth_mode: "raw.types.StoriesStealthMode"
    ) -> Optional["StoriesStealthMode"]:
        if stealth_mode is None:
            return None

        return StoriesStealthMode(
            client=client,
            active_until=utils.timestamp_to_datetime(stealth_mode.active_until_date),
            cooldown_until=utils.timestamp_to_datetime(stealth_mode.cooldown_until_date)
        )
