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


class DisallowedGiftsSettings(Object):
    """Disallow the reception of specific gift types.

    Parameters:
        disallow_unlimited_stargifts (``bool``, *optional*):
            Disallow the reception of gifts with an unlimited supply.

        disallow_limited_stargifts (``bool``, *optional*):
            Disallow the reception of limited-supply gifts.

        disallow_unique_stargifts (``bool``, *optional*):
            Disallow the reception of collectible gifts.

        disallow_premium_gifts (``bool``, *optional*):
            Disallow the reception of gifted Telegram Premium subscriptions.

        disallow_stargifts_from_channels (``bool``, *optional*):
            Disallow the reception of star gifts from channels.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        disallow_unlimited_stargifts: bool = None,
        disallow_limited_stargifts: bool = None,
        disallow_unique_stargifts: bool = None,
        disallow_premium_gifts: bool = None,
        disallow_stargifts_from_channels: bool = None
    ):
        super().__init__(client)

        self.disallow_unlimited_stargifts = disallow_unlimited_stargifts
        self.disallow_limited_stargifts = disallow_limited_stargifts
        self.disallow_unique_stargifts = disallow_unique_stargifts
        self.disallow_premium_gifts = disallow_premium_gifts
        self.disallow_stargifts_from_channels = disallow_stargifts_from_channels

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        settings: "raw.types.DisallowedGiftsSettings"
    ) -> Optional["DisallowedGiftsSettings"]:
        if not settings:
            return None

        return DisallowedGiftsSettings(
            client=client,
            disallow_unlimited_stargifts=settings.disallow_unlimited_stargifts,
            disallow_limited_stargifts=settings.disallow_limited_stargifts,
            disallow_unique_stargifts=settings.disallow_unique_stargifts,
            disallow_premium_gifts=settings.disallow_premium_gifts,
            disallow_stargifts_from_channels=settings.disallow_stargifts_from_channels
        )
