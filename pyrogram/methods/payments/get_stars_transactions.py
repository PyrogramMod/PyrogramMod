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

from typing import AsyncGenerator, Optional, Union

import pyrogram
from pyrogram import raw, types


class GetStarsTransactions:
    async def get_stars_transactions(
        self: "pyrogram.Client",
        peer: Union[int, str] = None,
        inbound: bool = None,
        outbound: bool = None,
        limit: int = 0,
        offset: str = ""
    ) -> AsyncGenerator["types.StarsTransaction", None]:
        """Get Stars transaction history.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            peer (``int`` | ``str``, *optional*):
                Unique identifier (int) or username (str) of the peer.
                If not provided, gets your own transaction history.

            inbound (``bool``, *optional*):
                If True, only get incoming transactions.

            outbound (``bool``, *optional*):
                If True, only get outgoing transactions.

            limit (``int``, *optional*):
                Limits the number of transactions to be retrieved.
                By default, no limit is applied and all transactions are returned.

            offset (``str``, *optional*):
                Pagination offset.

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.StarsTransaction` objects.

        Example:
            .. code-block:: python

                # Get all transactions
                async for transaction in app.get_stars_transactions():
                    print(transaction)

                # Get only incoming transactions
                async for transaction in app.get_stars_transactions(inbound=True):
                    print(f"Received {transaction.amount}")
        """
        if peer:
            input_peer = await self.resolve_peer(peer)
        else:
            input_peer = raw.types.InputPeerSelf()

        current = 0
        total = abs(limit) or (1 << 31) - 1
        limit = min(100, total)

        while True:
            r = await self.invoke(
                raw.functions.payments.GetStarsTransactions(
                    peer=input_peer,
                    inbound=inbound,
                    outbound=outbound,
                    offset=offset,
                    limit=limit
                )
            )

            users = {u.id: u for u in r.users}
            chats = {c.id: c for c in r.chats}

            transactions = r.history

            if not transactions:
                return

            for transaction in transactions:
                yield types.StarsTransaction._parse(self, transaction, users, chats)

                current += 1

                if current >= total:
                    return

            offset = r.next_offset

            if not offset:
                return
