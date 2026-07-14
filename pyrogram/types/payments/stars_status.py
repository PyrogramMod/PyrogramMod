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

from typing import List, Optional

import pyrogram
from pyrogram import raw, types
from ..object import Object


class StarsStatus(Object):
    """Represents the current Stars balance and transactions.

    Parameters:
        balance (:obj:`~pyrogram.types.StarsAmount`):
            Current Stars balance.

        subscriptions (List of :obj:`~pyrogram.types.StarsSubscription`, *optional*):
            Active subscriptions.

        subscriptions_next_offset (``str``, *optional*):
            Offset for fetching more subscriptions.

        subscriptions_missing_balance (``int``, *optional*):
            Amount of Stars missing for subscription renewal.

        history (List of :obj:`~pyrogram.types.StarsTransaction`, *optional*):
            Transaction history.

        history_next_offset (``str``, *optional*):
            Offset for fetching more history.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        balance: "types.StarsAmount" = None,
        subscriptions: List["types.StarsSubscription"] = None,
        subscriptions_next_offset: str = None,
        subscriptions_missing_balance: int = None,
        history: List["types.StarsTransaction"] = None,
        history_next_offset: str = None
    ):
        super().__init__(client)

        self.balance = balance
        self.subscriptions = subscriptions
        self.subscriptions_next_offset = subscriptions_next_offset
        self.subscriptions_missing_balance = subscriptions_missing_balance
        self.history = history
        self.history_next_offset = history_next_offset

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        status: "raw.types.payments.StarsStatus",
        users: dict = None,
        chats: dict = None
    ) -> "StarsStatus":
        from .stars_amount import StarsAmount
        from .stars_transaction import StarsTransaction
        from .stars_subscription import StarsSubscription

        if users is None:
            users = {u.id: u for u in status.users}
        if chats is None:
            chats = {c.id: c for c in status.chats}

        subscriptions = None
        if status.subscriptions:
            subscriptions = types.List([
                StarsSubscription._parse(client, s, users, chats)
                for s in status.subscriptions
            ])

        history = None
        if status.history:
            history = types.List([
                StarsTransaction._parse(client, t, users, chats)
                for t in status.history
            ])

        return StarsStatus(
            client=client,
            balance=StarsAmount._parse(client, status.balance),
            subscriptions=subscriptions,
            subscriptions_next_offset=status.subscriptions_next_offset,
            subscriptions_missing_balance=status.subscriptions_missing_balance,
            history=history,
            history_next_offset=status.next_offset
        )
