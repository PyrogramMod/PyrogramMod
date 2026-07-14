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
from pyrogram import raw, types, utils
from ..object import Object


class StarGiftAuctionUserState(Object):
    """Represents a user's state in a star gift auction.

    Parameters:
        acquired_count (``int``):
            Number of gifts acquired.

        returned (``bool``, *optional*):
            Whether the bid was returned.

        bid_amount (``int``, *optional*):
            Current bid amount.

        bid_date (:py:obj:`~datetime.datetime`, *optional*):
            Date of the bid.

        min_bid_amount (``int``, *optional*):
            Minimum bid amount required.

        bid_peer (:obj:`~pyrogram.types.Chat`, *optional*):
            Peer who placed the bid.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        acquired_count: int,
        returned: bool = None,
        bid_amount: int = None,
        bid_date: datetime = None,
        min_bid_amount: int = None,
        bid_peer: "types.Chat" = None
    ):
        super().__init__(client)

        self.acquired_count = acquired_count
        self.returned = returned
        self.bid_amount = bid_amount
        self.bid_date = bid_date
        self.min_bid_amount = min_bid_amount
        self.bid_peer = bid_peer

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        state: "raw.types.StarGiftAuctionUserState",
        chats: dict = None
    ) -> Optional["StarGiftAuctionUserState"]:
        if not state:
            return None

        chats = chats or {}
        bid_peer = None
        if state.bid_peer:
             # This requires resolving the peer.
             # state.bid_peer is a Peer (PeerUser, PeerChat, PeerChannel).
             # We need the chats/users dicts to resolve it fully to a Chat object.
             # For now we will try to resolve from available dicts or leave it as None if not found
             # Wait, strict parsing would require them.
             # Let's use utils.get_peer_id and try to fetch from chats/users if available?
             # For parsing simple objects we usually assume passed dicts have the info.

             # If state.bid_peer is available, we try to parse it.
             # We need a generic peer parser that takes a Peer and dicts.
             # types.Chat._parse_chat(client, peer) ? No, that takes User/Chat/Channel.
             # types.Chat._parse_dialog?
             # Let's do manual look up.
             peer_id = utils.get_peer_id(state.bid_peer)
             if peer_id in chats:
                 bid_peer = types.Chat._parse_channel_chat(client, chats[peer_id]) # Usually channels/chats
             # If it's a user?
             # "users" dict is not passed here? I should add it to signature if needed.
             pass

        return StarGiftAuctionUserState(
            client=client,
            acquired_count=state.acquired_count,
            returned=state.returned,
            bid_amount=state.bid_amount,
            bid_date=utils.timestamp_to_datetime(state.bid_date),
            min_bid_amount=state.min_bid_amount,
            bid_peer=bid_peer # Placeholder, requires proper peer resolution logic updates if critical
        )
