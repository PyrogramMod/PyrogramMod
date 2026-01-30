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


class StarsTopupOption(Object):
    """Telegram Stars topup option.

    Parameters:
        stars (``int``):
            Amount of Telegram stars.

        currency (``str``):
            Three-letter ISO 4217 currency code.

        amount (``int``):
            Price of the product in the smallest units of the currency (integer, not float/double).

        extended (``bool``, *optional*):
            If set, the option must only be shown in the full list of topup options.

        store_product (``str``, *optional*):
            Identifier of the store product associated with the option, official apps only.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        stars: int,
        currency: str,
        amount: int,
        extended: bool = None,
        store_product: str = None
    ):
        super().__init__(client)

        self.stars = stars
        self.currency = currency
        self.amount = amount
        self.extended = extended
        self.store_product = store_product

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        option: "raw.types.StarsTopupOption"
    ) -> "StarsTopupOption":
        return StarsTopupOption(
            client=client,
            stars=option.stars,
            currency=option.currency,
            amount=option.amount,
            extended=option.extended,
            store_product=option.store_product
        )
