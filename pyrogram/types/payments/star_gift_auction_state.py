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
from typing import List, Optional, Union

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class StarGiftAuctionState(Object):
    """Represents the state of a star gift auction.

    Parameters:
        type (``str``):
            State type: "active", "finished", or "not_modified".

        version (``int``, *optional*):
            State version number.

        start_date (:py:obj:`~datetime.datetime`, *optional*):
            Auction start date.

        end_date (:py:obj:`~datetime.datetime`, *optional*):
            Auction end date.

        min_bid_amount (``int``, *optional*):
            Minimum bid amount required.

        bid_levels (List of :obj:`~pyrogram.types.AuctionBidLevel`, *optional*):
            Current bid levels in the auction.

        top_bidders (List of ``int``, *optional*):
            User IDs of top bidders.

        next_round_at (:py:obj:`~datetime.datetime`, *optional*):
            Date of the next round.

        last_gift_num (``int``, *optional*):
            Number of the last gift.

        gifts_left (``int``, *optional*):
            Number of gifts remaining.

        current_round (``int``, *optional*):
            Current round number.

        total_rounds (``int``, *optional*):
            Total number of rounds.

        rounds (List of :obj:`~pyrogram.types.StarGiftAuctionRound`, *optional*):
            Information about auction rounds.

        average_price (``int``, *optional*):
            Average price (for finished auctions).

        listed_count (``int``, *optional*):
            Number of gifts listed (for finished auctions).

        fragment_listed_count (``int``, *optional*):
            Number of gifts listed on Fragment (for finished auctions).

        fragment_listed_url (``str``, *optional*):
            URL for Fragment listing (for finished auctions).
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        type: str,
        version: int = None,
        start_date: datetime = None,
        end_date: datetime = None,
        min_bid_amount: int = None,
        bid_levels: List["types.AuctionBidLevel"] = None,
        top_bidders: List[int] = None,
        next_round_at: datetime = None,
        last_gift_num: int = None,
        gifts_left: int = None,
        current_round: int = None,
        total_rounds: int = None,
        rounds: List["types.StarGiftAuctionRound"] = None,
        average_price: int = None,
        listed_count: int = None,
        fragment_listed_count: int = None,
        fragment_listed_url: str = None
    ):
        super().__init__(client)

        self.type = type
        self.version = version
        self.start_date = start_date
        self.end_date = end_date
        self.min_bid_amount = min_bid_amount
        self.bid_levels = bid_levels
        self.top_bidders = top_bidders
        self.next_round_at = next_round_at
        self.last_gift_num = last_gift_num
        self.gifts_left = gifts_left
        self.current_round = current_round
        self.total_rounds = total_rounds
        self.rounds = rounds
        self.average_price = average_price
        self.listed_count = listed_count
        self.fragment_listed_count = fragment_listed_count
        self.fragment_listed_url = fragment_listed_url

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        state: Union["raw.types.StarGiftAuctionState", "raw.types.StarGiftAuctionStateFinished", "raw.types.StarGiftAuctionStateNotModified"]
    ) -> Optional["StarGiftAuctionState"]:
        if not state:
            return None

        if isinstance(state, raw.types.StarGiftAuctionStateNotModified):
            return StarGiftAuctionState(
                client=client,
                type="not_modified"
            )

        elif isinstance(state, raw.types.StarGiftAuctionStateFinished):
            return StarGiftAuctionState(
                client=client,
                type="finished",
                start_date=utils.timestamp_to_datetime(state.start_date),
                end_date=utils.timestamp_to_datetime(state.end_date),
                average_price=state.average_price,
                listed_count=state.listed_count,
                fragment_listed_count=state.fragment_listed_count,
                fragment_listed_url=state.fragment_listed_url
            )

        elif isinstance(state, raw.types.StarGiftAuctionState):
            return StarGiftAuctionState(
                client=client,
                type="active",
                version=state.version,
                start_date=utils.timestamp_to_datetime(state.start_date),
                end_date=utils.timestamp_to_datetime(state.end_date),
                min_bid_amount=state.min_bid_amount,
                bid_levels=types.List([
                    types.AuctionBidLevel._parse(client, level)
                    for level in state.bid_levels
                ]) if state.bid_levels else None,
                top_bidders=state.top_bidders,
                next_round_at=utils.timestamp_to_datetime(state.next_round_at),
                last_gift_num=state.last_gift_num,
                gifts_left=state.gifts_left,
                current_round=state.current_round,
                total_rounds=state.total_rounds,
                rounds=types.List([
                    types.StarGiftAuctionRound._parse(client, round)
                    for round in state.rounds
                ]) if state.rounds else None
            )

        return None
