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
from pyrogram import raw, types


class GetStarGiftAuctionState:
    async def get_star_gift_auction_state(
        self: "pyrogram.Client",
        gift_id: int
    ) -> "types.StarGiftAuctionState":
        """Get the auction state of a unique star gift.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            gift_id (``int``):
                The unique ID of the gift.

        Returns:
            :obj:`~pyrogram.types.StarGiftAuctionState`: On success, the auction state is returned.
        """
        r = await self.invoke(
            raw.functions.payments.GetStarGiftAuctionState(
                auction=raw.types.InputStarGiftAuction(gift_id=gift_id),
                version=0
            )
        )
        return types.StarGiftAuctionState._parse(self, r)
