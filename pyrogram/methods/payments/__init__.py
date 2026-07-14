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

from .get_stars_status import GetStarsStatus
from .get_stars_transactions import GetStarsTransactions
from .get_star_gifts import GetStarGifts
from .get_unique_star_gift import GetUniqueStarGift
from .get_saved_star_gifts import GetSavedStarGifts
from .get_star_gift_auction_state import GetStarGiftAuctionState


class Payments(
    GetStarsStatus,
    GetStarsTransactions,
    GetStarGifts,
    GetUniqueStarGift,
    GetSavedStarGifts,
    GetStarGiftAuctionState
):
    pass
