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


class AuctionBidLevel(Object):
    """Represents an auction bid level.

    Parameters:
        position (``int``):
            Bid position.

        amount (``int``):
            Bid amount.

        date (:py:obj:`~datetime.datetime`, *optional*):
            Date of the bid.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        position: int,
        amount: int,
        date: datetime = None
    ):
        super().__init__(client)

        self.position = position
        self.amount = amount
        self.date = date

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        level: "raw.types.AuctionBidLevel"
    ) -> "AuctionBidLevel":
        return AuctionBidLevel(
            client=client,
            position=level.pos,
            amount=level.amount,
            date=utils.timestamp_to_datetime(level.date)
        )
