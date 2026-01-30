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


class StarsSubscriptionPricing(Object):
    """Represents the pricing of a Stars subscription.

    Parameters:
        period (``int``):
            Subscription period in seconds.

        amount (:obj:`~pyrogram.types.StarsAmount`):
            Amount of Stars for this subscription period.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        period: int,
        amount: "types.StarsAmount" = None
    ):
        super().__init__(client)

        self.period = period
        self.amount = amount

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        pricing: "raw.types.StarsSubscriptionPricing"
    ) -> "StarsSubscriptionPricing":
        from .stars_amount import StarsAmount

        if pricing is None:
            return None

        return StarsSubscriptionPricing(
            client=client,
            period=pricing.period,
            amount=StarsAmount._parse_int(client, pricing.amount)
        )


class StarsSubscription(Object):
    """Represents a Telegram Stars subscription.

    Parameters:
        id (``str``):
            Subscription ID.

        peer (:obj:`~pyrogram.types.User` | :obj:`~pyrogram.types.Chat`):
            The peer (user or chat) associated with this subscription.

        until_date (:py:obj:`~datetime.datetime`):
            Expiration date of the current subscription period.

        pricing (:obj:`~pyrogram.types.StarsSubscriptionPricing`):
            Pricing of the subscription.

        title (``str``, *optional*):
            Title of the subscription (for bot subscriptions).

        is_canceled (``bool``, *optional*):
            Whether this subscription was canceled.

        can_refulfill (``bool``, *optional*):
            Whether we left the channel but can still rejoin.

        missing_balance (``bool``, *optional*):
            Whether the subscription expired due to insufficient balance.

        bot_canceled (``bool``, *optional*):
            Whether the bot canceled this subscription.

        chat_invite_hash (``str``, *optional*):
            Invitation link to renew after cancellation.

        invoice_slug (``str``, *optional*):
            For bot subscriptions, the invoice identifier.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        peer: "types.User" = None,
        until_date: datetime = None,
        pricing: "StarsSubscriptionPricing" = None,
        title: str = None,
        is_canceled: bool = None,
        can_refulfill: bool = None,
        missing_balance: bool = None,
        bot_canceled: bool = None,
        chat_invite_hash: str = None,
        invoice_slug: str = None
    ):
        super().__init__(client)

        self.id = id
        self.peer = peer
        self.until_date = until_date
        self.pricing = pricing
        self.title = title
        self.is_canceled = is_canceled
        self.can_refulfill = can_refulfill
        self.missing_balance = missing_balance
        self.bot_canceled = bot_canceled
        self.chat_invite_hash = chat_invite_hash
        self.invoice_slug = invoice_slug

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        subscription: "raw.types.StarsSubscription",
        users: dict,
        chats: dict
    ) -> "StarsSubscription":
        peer = None
        if isinstance(subscription.peer, raw.types.PeerUser):
            peer = types.User._parse(client, users.get(subscription.peer.user_id))
        elif isinstance(subscription.peer, raw.types.PeerChannel):
            peer = types.Chat._parse_channel_chat(client, chats.get(subscription.peer.channel_id))
        elif isinstance(subscription.peer, raw.types.PeerChat):
            peer = types.Chat._parse_chat_chat(client, chats.get(subscription.peer.chat_id))

        return StarsSubscription(
            client=client,
            id=subscription.id,
            peer=peer,
            until_date=utils.timestamp_to_datetime(subscription.until_date),
            pricing=StarsSubscriptionPricing._parse(client, subscription.pricing),
            title=subscription.title,
            is_canceled=subscription.canceled or None,
            can_refulfill=subscription.can_refulfill or None,
            missing_balance=subscription.missing_balance or None,
            bot_canceled=subscription.bot_canceled or None,
            chat_invite_hash=subscription.chat_invite_hash,
            invoice_slug=subscription.invoice_slug
        )
