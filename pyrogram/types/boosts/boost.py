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


class Boost(Object):
    """Represents a channel boost.

    Parameters:
        id (``str``):
            Unique identifier of the boost.

        user (:obj:`~pyrogram.types.User`, *optional*):
            The user who boosted (if not from a giveaway).

        date (:py:obj:`~datetime.datetime`):
            When the boost was applied.

        expires (:py:obj:`~datetime.datetime`):
            When the boost expires.

        giveaway_message_id (``int``, *optional*):
            For giveaway boosts: the giveaway message ID.

        stars (``int``, *optional*):
            For Telegram Stars boosts: amount of stars used.

        multiplier (``int``, *optional*):
            Boost multiplier (for Telegram Premium users).

        is_gift (``bool``, *optional*):
            Whether this boost was a gift.

        is_giveaway (``bool``, *optional*):
            Whether this boost is from a giveaway.

        is_unclaimed (``bool``, *optional*):
            Whether this giveaway boost was unclaimed.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        user: "types.User" = None,
        date: datetime = None,
        expires: datetime = None,
        giveaway_message_id: int = None,
        stars: int = None,
        multiplier: int = None,
        is_gift: bool = None,
        is_giveaway: bool = None,
        is_unclaimed: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.user = user
        self.date = date
        self.expires = expires
        self.giveaway_message_id = giveaway_message_id
        self.stars = stars
        self.multiplier = multiplier
        self.is_gift = is_gift
        self.is_giveaway = is_giveaway
        self.is_unclaimed = is_unclaimed

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        boost: "raw.types.Boost",
        users: dict
    ) -> "Boost":
        user = None
        if boost.user_id and boost.user_id in users:
            user = types.User._parse(client, users[boost.user_id])

        return Boost(
            client=client,
            id=boost.id,
            user=user,
            date=utils.timestamp_to_datetime(boost.date),
            expires=utils.timestamp_to_datetime(boost.expires),
            giveaway_message_id=boost.giveaway_msg_id,
            stars=boost.stars,
            multiplier=boost.multiplier,
            is_gift=boost.gift or None,
            is_giveaway=boost.giveaway or None,
            is_unclaimed=boost.unclaimed or None
        )

    @staticmethod
    def _parse_list(
        client: "pyrogram.Client",
        boosts: list,
        users: dict
    ) -> list:
        return types.List([
            Boost._parse(client, b, users)
            for b in boosts
        ])
