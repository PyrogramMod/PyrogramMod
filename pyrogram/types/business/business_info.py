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

from typing import Optional

import pyrogram
from pyrogram import raw, types
from ..object import Object

from .business_hours import BusinessWorkHours
from .business_location import BusinessLocation
from .business_intro import BusinessIntro
from .business_message import BusinessGreetingMessage, BusinessAwayMessage


class BusinessInfo(Object):
    """Aggregated business information for a user.

    Parameters:
        work_hours (:obj:`~pyrogram.types.BusinessWorkHours`, *optional*):
            Business work hours.

        location (:obj:`~pyrogram.types.BusinessLocation`, *optional*):
            Business location.

        intro (:obj:`~pyrogram.types.BusinessIntro`, *optional*):
            Business introduction.

        greeting_message (:obj:`~pyrogram.types.BusinessGreetingMessage`, *optional*):
            Automated greeting message settings.

        away_message (:obj:`~pyrogram.types.BusinessAwayMessage`, *optional*):
            Automated away message settings.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        work_hours: "BusinessWorkHours" = None,
        location: "BusinessLocation" = None,
        intro: "BusinessIntro" = None,
        greeting_message: "BusinessGreetingMessage" = None,
        away_message: "BusinessAwayMessage" = None
    ):
        super().__init__(client)

        self.work_hours = work_hours
        self.location = location
        self.intro = intro
        self.greeting_message = greeting_message
        self.away_message = away_message

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        user_full: "raw.types.UserFull"
    ) -> Optional["BusinessInfo"]:
        """Parse business info from a UserFull object."""

        work_hours = BusinessWorkHours._parse(client, getattr(user_full, 'business_work_hours', None))
        location = BusinessLocation._parse(client, getattr(user_full, 'business_location', None))
        intro = await BusinessIntro._parse(client, getattr(user_full, 'business_intro', None))
        greeting_message = BusinessGreetingMessage._parse(client, getattr(user_full, 'business_greeting_message', None))
        away_message = BusinessAwayMessage._parse(client, getattr(user_full, 'business_away_message', None))

        # Return None if no business info is available
        if not any([work_hours, location, intro, greeting_message, away_message]):
            return None

        return BusinessInfo(
            client=client,
            work_hours=work_hours,
            location=location,
            intro=intro,
            greeting_message=greeting_message,
            away_message=away_message
        )
