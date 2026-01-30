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

import pyrogram
from pyrogram import raw
from ..object import Object


class PremiumGiftCodeOption(Object):
    """A premium gift code option.

    Parameters:
        users (``int``):
            Number of users this option is for.

        months (``int``):
            Duration of the subscription in months.

        currency (``str``):
            Three-letter ISO 4217 currency code.

        amount (``int``):
            Price in the smallest units of the currency.

        store_product (``str``, *optional*):
            Identifier of the store product.

        store_quantity (``int``, *optional*):
            Store quantity.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        users: int,
        months: int,
        currency: str,
        amount: int,
        store_product: str = None,
        store_quantity: int = None
    ):
        super().__init__(client)

        self.users = users
        self.months = months
        self.currency = currency
        self.amount = amount
        self.store_product = store_product
        self.store_quantity = store_quantity

    @staticmethod
    def _parse(client: "pyrogram.Client", option: "raw.types.PremiumGiftCodeOption") -> "PremiumGiftCodeOption":
        if not option:
            return None

        return PremiumGiftCodeOption(
            client=client,
            users=option.users,
            months=option.months,
            currency=option.currency,
            amount=option.amount,
            store_product=getattr(option, "store_product", None),
            store_quantity=getattr(option, "store_quantity", None)
        )
