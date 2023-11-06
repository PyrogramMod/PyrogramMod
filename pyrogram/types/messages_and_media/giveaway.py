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


class Giveaway(Object):
    """A Giveaway.

    Parameters:
        client (pyrogram.Client): Pyrogram client
        channels (List of ``int`` ``64-bit``):
        quantity (``int`` ``32-bit``):
        months (``int`` ``32-bit``):
        until_date (``int`` ``32-bit``):
        only_new_subscribers (``bool``, *optional*):
        countries_iso2 (List of ``str``, *optional*):

    """

    def __init__(
            self,
            *,
            client: "pyrogram.Client" = None,
            channels,
            quantity,
            months,
            until_date,
            only_new_subscribers,
            countries_iso2,
    ):
        super().__init__(client)

        self.channels = channels
        self.quantity = quantity
        self.months = months
        self.until_date = until_date
        self.only_new_subscribers = only_new_subscribers
        self.countries_iso2 = countries_iso2

    @staticmethod
    def _parse(client, giveaway: "raw.types.MessageMediaGiveaway"):
        return Giveaway(
            client=client,
            channels=giveaway.channels,
            quantity=giveaway.quantity,
            months=giveaway.months,
            until_date=giveaway.until_date,
            only_new_subscribers=giveaway.only_new_subscribers,
            countries_iso2=giveaway.countries_iso2
        )
