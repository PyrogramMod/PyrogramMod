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

from typing import List, Optional

import pyrogram
from pyrogram import raw
from ..object import Object


class BusinessWeeklyOpen(Object):
    """Represents a time interval during which a business is open.

    Parameters:
        start_minute (``int``):
            Start time of the open interval, in minutes from the start of the week
            (Monday 00:00). Range: 0-10080 (7 days * 24 hours * 60 minutes).

        end_minute (``int``):
            End time of the open interval, in minutes from the start of the week.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        start_minute: int,
        end_minute: int
    ):
        super().__init__(client)

        self.start_minute = start_minute
        self.end_minute = end_minute

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        weekly_open: "raw.types.BusinessWeeklyOpen"
    ) -> "BusinessWeeklyOpen":
        return BusinessWeeklyOpen(
            client=client,
            start_minute=weekly_open.start_minute,
            end_minute=weekly_open.end_minute
        )


class BusinessWorkHours(Object):
    """Represents the work hours of a business.

    Parameters:
        timezone_id (``str``):
            Timezone ID (e.g., "Europe/Rome", "America/New_York").

        weekly_open (List of :obj:`~pyrogram.types.BusinessWeeklyOpen`):
            List of time intervals during which the business is open.

        open_now (``bool``, *optional*):
            Whether the business is currently open.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        timezone_id: str,
        weekly_open: List["BusinessWeeklyOpen"] = None,
        open_now: bool = None
    ):
        super().__init__(client)

        self.timezone_id = timezone_id
        self.weekly_open = weekly_open
        self.open_now = open_now

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        work_hours: "raw.types.BusinessWorkHours"
    ) -> Optional["BusinessWorkHours"]:
        if work_hours is None:
            return None

        from pyrogram import types

        weekly_open = types.List([
            BusinessWeeklyOpen._parse(client, wo)
            for wo in work_hours.weekly_open
        ]) if work_hours.weekly_open else None

        return BusinessWorkHours(
            client=client,
            timezone_id=work_hours.timezone_id,
            weekly_open=weekly_open,
            open_now=work_hours.open_now or None
        )
