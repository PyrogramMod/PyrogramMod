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

from typing import Union

import pyrogram
from pyrogram import raw
from ..object import Object


class StarsAmount(Object):
    """Represents an amount of Telegram Stars with nano precision.

    Parameters:
        amount (``int``):
            The integer amount of Telegram Stars.

        nanos (``int``):
            The decimal amount of Telegram Stars, expressed as nanostars.
            1 nanostar = 1/1,000,000,000 (one billionth) of a Star.
            Range: -999999999 to 999999999.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        amount: int,
        nanos: int = 0
    ):
        super().__init__(client)

        self.amount = amount
        self.nanos = nanos

    @property
    def total(self) -> float:
        """Get the total amount as a float including nanostars."""
        return self.amount + (self.nanos / 1_000_000_000)

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        stars_amount: "raw.types.StarsAmount"
    ) -> "StarsAmount":
        if stars_amount is None:
            return None

        return StarsAmount(
            client=client,
            amount=stars_amount.amount,
            nanos=stars_amount.nanos
        )

    @staticmethod
    def _parse_int(
        client: "pyrogram.Client",
        amount: int
    ) -> "StarsAmount":
        """Parse a simple integer amount to StarsAmount."""
        return StarsAmount(
            client=client,
            amount=amount,
            nanos=0
        )

    def __repr__(self) -> str:
        if self.nanos:
            return f"StarsAmount(amount={self.amount}, nanos={self.nanos})"
        return f"StarsAmount(amount={self.amount})"

    def __str__(self) -> str:
        if self.nanos:
            return f"{self.total:.9f} Stars"
        return f"{self.amount} Stars"
