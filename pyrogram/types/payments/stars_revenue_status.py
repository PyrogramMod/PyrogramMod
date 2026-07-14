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


class StarsRevenueStatus(Object):
    """Describes Telegram Star revenue balances.

    Parameters:
        current_balance (:obj:`~pyrogram.types.StarsAmount`):
            Amount of not-yet-withdrawn Telegram Stars.

        available_balance (:obj:`~pyrogram.types.StarsAmount`):
            Amount of withdrawable Telegram Stars.

        overall_revenue (:obj:`~pyrogram.types.StarsAmount`):
            Total amount of earned Telegram Stars.

        withdrawal_enabled (``bool``):
            If set, the user may withdraw up to available_balance stars.

        next_withdrawal_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when withdrawal will be available to the user. If not set, withdrawal can be started now.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        current_balance: "types.StarsAmount",
        available_balance: "types.StarsAmount",
        overall_revenue: "types.StarsAmount",
        withdrawal_enabled: bool,
        next_withdrawal_date: datetime = None
    ):
        super().__init__(client)

        self.current_balance = current_balance
        self.available_balance = available_balance
        self.overall_revenue = overall_revenue
        self.withdrawal_enabled = withdrawal_enabled
        self.next_withdrawal_date = next_withdrawal_date

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        status: "raw.types.StarsRevenueStatus"
    ) -> "StarsRevenueStatus":
        return StarsRevenueStatus(
            client=client,
            current_balance=types.StarsAmount._parse(client, status.current_balance),
            available_balance=types.StarsAmount._parse(client, status.available_balance),
            overall_revenue=types.StarsAmount._parse(client, status.overall_revenue),
            withdrawal_enabled=status.withdrawal_enabled,
            next_withdrawal_date=utils.timestamp_to_datetime(status.next_withdrawal_at)
        )
