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


class Staking:
    async def get_staking_info(
        self: "pyrogram.Client"
    ) -> "raw.types.WalletStakingInfo":
        """Get the TON staking state of your Telegram wallet.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            :obj:`~pyrogram.raw.types.WalletStakingInfo`: The raw state: APR, staked, available and pending amounts.

        Example:
            .. code-block:: python

                info = await app.get_staking_info()
                print(info.apr, info.staked)
        """
        return await self.invoke(raw.functions.wallet.GetStakingInfo())

    async def stake(
        self: "pyrogram.Client",
        amount: Optional[int] = None
    ) -> "raw.types.WalletStakingPrepared":
        """Prepare a TON staking deposit.

        Telegram only prepares the transfer: sign and send it with your wallet.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            amount (``int``, *optional*):
                Amount in nanotons. Pass None to stake the whole balance.

        Returns:
            :obj:`~pyrogram.raw.types.WalletStakingPrepared`: The raw transfer (destination, value and body).

        Example:
            .. code-block:: python

                tx = await app.stake(1_000_000_000)
        """
        return await self.invoke(
            raw.functions.wallet.Stake(amount=amount or 0, stake_all=amount is None)
        )

    async def unstake(
        self: "pyrogram.Client",
        amount: Optional[int] = None
    ) -> "raw.types.WalletStakingPrepared":
        """Prepare a TON staking withdrawal.

        Telegram only prepares the transfer: sign and send it with your wallet.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            amount (``int``, *optional*):
                Amount in nanotons. Pass None to withdraw everything.

        Returns:
            :obj:`~pyrogram.raw.types.WalletStakingPrepared`: The raw transfer (destination, value and body).

        Example:
            .. code-block:: python

                tx = await app.unstake()
        """
        return await self.invoke(
            raw.functions.wallet.Unstake(amount=amount or 0, withdraw_all=amount is None)
        )
