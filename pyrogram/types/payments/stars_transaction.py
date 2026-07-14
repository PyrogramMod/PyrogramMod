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


class StarsTransactionPeer(Object):
    """Represents the peer involved in a Stars transaction.

    Parameters:
        type (``str``):
            Type of the peer. Can be one of:
            - "user": A user
            - "channel": A channel/supergroup
            - "app_store": Apple App Store
            - "play_market": Google Play Market
            - "fragment": Fragment
            - "premium_bot": Premium Bot
            - "ads": Telegram Ads
            - "api": Telegram API usage
            - "unsupported": Unsupported peer type

        user (:obj:`~pyrogram.types.User`, *optional*):
            For "user" type, the user.

        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            For "channel" type, the chat.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        type: str,
        user: "types.User" = None,
        chat: "types.Chat" = None
    ):
        super().__init__(client)

        self.type = type
        self.user = user
        self.chat = chat

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        peer: "raw.base.StarsTransactionPeer",
        users: dict,
        chats: dict
    ) -> "StarsTransactionPeer":
        if isinstance(peer, raw.types.StarsTransactionPeer):
            if isinstance(peer.peer, raw.types.PeerUser):
                return StarsTransactionPeer(
                    client=client,
                    type="user",
                    user=types.User._parse(client, users.get(peer.peer.user_id))
                )
            elif isinstance(peer.peer, raw.types.PeerChannel):
                return StarsTransactionPeer(
                    client=client,
                    type="channel",
                    chat=types.Chat._parse_channel_chat(client, chats.get(peer.peer.channel_id))
                )
            elif isinstance(peer.peer, raw.types.PeerChat):
                return StarsTransactionPeer(
                    client=client,
                    type="channel",
                    chat=types.Chat._parse_chat_chat(client, chats.get(peer.peer.chat_id))
                )
        elif isinstance(peer, raw.types.StarsTransactionPeerAppStore):
            return StarsTransactionPeer(client=client, type="app_store")
        elif isinstance(peer, raw.types.StarsTransactionPeerPlayMarket):
            return StarsTransactionPeer(client=client, type="play_market")
        elif isinstance(peer, raw.types.StarsTransactionPeerFragment):
            return StarsTransactionPeer(client=client, type="fragment")
        elif isinstance(peer, raw.types.StarsTransactionPeerPremiumBot):
            return StarsTransactionPeer(client=client, type="premium_bot")
        elif isinstance(peer, raw.types.StarsTransactionPeerAds):
            return StarsTransactionPeer(client=client, type="ads")
        elif isinstance(peer, raw.types.StarsTransactionPeerApi):
            return StarsTransactionPeer(client=client, type="api")

        return StarsTransactionPeer(client=client, type="unsupported")


class StarsTransaction(Object):
    """Represents a Telegram Stars transaction.

    Parameters:
        id (``str``):
            Transaction ID.

        amount (:obj:`~pyrogram.types.StarsAmount`):
            Amount of Stars in this transaction.

        date (:py:obj:`~datetime.datetime`):
            Date of the transaction.

        peer (:obj:`~pyrogram.types.StarsTransactionPeer`):
            Source of incoming transaction, or recipient for outgoing.

        title (``str``, *optional*):
            Title of the transaction (for bot/channel subscriptions).

        description (``str``, *optional*):
            Description of the transaction.

        is_refund (``bool``, *optional*):
            Whether this is a refund transaction.

        is_pending (``bool``, *optional*):
            Whether this transaction is pending.

        is_failed (``bool``, *optional*):
            Whether this transaction failed.

        is_gift (``bool``, *optional*):
            Whether this was a gift from the peer.

        is_reaction (``bool``, *optional*):
            Whether this was a paid reaction.

        is_subscription (``bool``, *optional*):
            Whether this is a subscription payment.

        transaction_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when the transaction was completed.

        transaction_url (``str``, *optional*):
            URL for more details about the transaction.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        amount: "types.StarsAmount" = None,
        date: datetime = None,
        peer: "StarsTransactionPeer" = None,
        title: str = None,
        description: str = None,
        is_refund: bool = None,
        is_pending: bool = None,
        is_failed: bool = None,
        is_gift: bool = None,
        is_reaction: bool = None,
        is_subscription: bool = None,
        transaction_date: datetime = None,
        transaction_url: str = None
    ):
        super().__init__(client)

        self.id = id
        self.amount = amount
        self.date = date
        self.peer = peer
        self.title = title
        self.description = description
        self.is_refund = is_refund
        self.is_pending = is_pending
        self.is_failed = is_failed
        self.is_gift = is_gift
        self.is_reaction = is_reaction
        self.is_subscription = is_subscription
        self.transaction_date = transaction_date
        self.transaction_url = transaction_url

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        transaction: "raw.types.StarsTransaction",
        users: dict,
        chats: dict
    ) -> "StarsTransaction":
        from .stars_amount import StarsAmount

        return StarsTransaction(
            client=client,
            id=transaction.id,
            amount=StarsAmount._parse(client, transaction.amount),
            date=utils.timestamp_to_datetime(transaction.date),
            peer=StarsTransactionPeer._parse(client, transaction.peer, users, chats),
            title=transaction.title,
            description=transaction.description,
            is_refund=transaction.refund or None,
            is_pending=transaction.pending or None,
            is_failed=transaction.failed or None,
            is_gift=transaction.gift or None,
            is_reaction=transaction.reaction or None,
            is_subscription=transaction.subscription or None,
            transaction_date=utils.timestamp_to_datetime(transaction.transaction_date),
            transaction_url=transaction.transaction_url
        )
