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
from pyrogram import raw
from ..object import Object


class StarGiftAuctionRound(Object):
    """Represents a star gift auction round.

    Parameters:
        num (``int``):
            Round number.

        duration (``int``):
            Round duration in seconds.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        num: int,
        duration: int
    ):
        super().__init__(client)

        self.num = num
        self.duration = duration

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        round: "raw.types.StarGiftAuctionRound"
    ) -> "StarGiftAuctionRound":
        return StarGiftAuctionRound(
            client=client,
            num=round.num,
            duration=round.duration
        )
