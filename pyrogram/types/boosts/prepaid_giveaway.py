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

import pyrogram
from pyrogram import raw, utils
from ..object import Object


class PrepaidGiveaway(Object):
    """Represents a prepaid giveaway.

    Parameters:
        id (``str``):
            Unique identifier of the prepaid giveaway.

        quantity (``int``):
            Number of giveaway prizes.

        months (``int``, *optional*):
            Number of months of Premium subscription as prize.

        stars (``int``, *optional*):
            Amount of Telegram Stars as prize.

        date (:py:obj:`~datetime.datetime`):
            When the giveaway was prepaid.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str = None,
        quantity: int = None,
        months: int = None,
        stars: int = None,
        date: datetime = None
    ):
        super().__init__(client)

        self.id = id
        self.quantity = quantity
        self.months = months
        self.stars = stars
        self.date = date

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        giveaway: "raw.types.PrepaidGiveaway"
    ) -> "PrepaidGiveaway":
        return PrepaidGiveaway(
            client=client,
            id=str(giveaway.id),
            quantity=giveaway.quantity,
            months=giveaway.months if hasattr(giveaway, 'months') else None,
            stars=giveaway.stars if hasattr(giveaway, 'stars') else None,
            date=utils.timestamp_to_datetime(giveaway.date)
        )
