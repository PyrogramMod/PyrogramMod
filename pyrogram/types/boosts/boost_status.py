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

from typing import Optional, List

import pyrogram
from pyrogram import raw, types
from ..object import Object


class BoostStatus(Object):
    """Represents a channel's boost status.

    Parameters:
        level (``int``):
            Current boost level of the channel.

        current_level_boosts (``int``):
            Number of boosts at current level.

        boosts (``int``):
            Total number of boosts.

        next_level_boosts (``int``, *optional*):
            Boosts needed for next level.

        premium_audience_percent (``float``, *optional*):
            Percentage of premium audience.

        prepaid_giveaways (List of :obj:`~pyrogram.types.PrepaidGiveaway`, *optional*):
            List of prepaid giveaways.

        my_boost (``bool``, *optional*):
            Whether the current user has boosted.

        my_boost_slots (List of ``int``, *optional*):
            Boost slots used by current user.

        boost_url (``str``, *optional*):
            URL for boosting the channel.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        level: int = None,
        current_level_boosts: int = None,
        boosts: int = None,
        next_level_boosts: int = None,
        premium_audience_percent: float = None,
        prepaid_giveaways: List["types.PrepaidGiveaway"] = None,
        my_boost: bool = None,
        my_boost_slots: List[int] = None,
        boost_url: str = None
    ):
        super().__init__(client)

        self.level = level
        self.current_level_boosts = current_level_boosts
        self.boosts = boosts
        self.next_level_boosts = next_level_boosts
        self.premium_audience_percent = premium_audience_percent
        self.prepaid_giveaways = prepaid_giveaways
        self.my_boost = my_boost
        self.my_boost_slots = my_boost_slots
        self.boost_url = boost_url

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        status: "raw.types.premium.BoostsStatus"
    ) -> "BoostStatus":
        prepaid = None
        if hasattr(status, 'prepaid_giveaways') and status.prepaid_giveaways:
            prepaid = [
                types.PrepaidGiveaway._parse(client, g)
                for g in status.prepaid_giveaways
            ]

        return BoostStatus(
            client=client,
            level=status.level,
            current_level_boosts=status.current_level_boosts,
            boosts=status.boosts,
            next_level_boosts=status.next_level_boosts if hasattr(status, 'next_level_boosts') else None,
            premium_audience_percent=status.premium_audience.part if hasattr(status, 'premium_audience') and status.premium_audience else None,
            prepaid_giveaways=types.List(prepaid) if prepaid else None,
            my_boost=status.my_boost or None,
            my_boost_slots=list(status.my_boost_slots) if hasattr(status, 'my_boost_slots') and status.my_boost_slots else None,
            boost_url=status.boost_url if hasattr(status, 'boost_url') else None
        )
