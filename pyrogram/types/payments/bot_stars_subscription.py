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
from ..object import Object
from ..update import Update


class BotStarsSubscription(Object, Update):
    """A bot stars subscription update.

    Parameters:
        user_id (``int``):
            The user ID whose subscription changed.

        payload (``bytes``):
            The subscription payload.

        qts (``int``):
            QTS (query time sequence).

        canceled (``bool``, *optional*):
            True if the subscription was canceled.

        payment_failed (``bool``, *optional*):
            True if the payment failed.

        restored (``bool``, *optional*):
            True if the subscription was restored.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        user_id: int,
        payload: bytes,
        qts: int,
        canceled: Optional[bool] = None,
        payment_failed: Optional[bool] = None,
        restored: Optional[bool] = None,
    ):
        super().__init__(client)
        self.user_id = user_id
        self.payload = payload
        self.qts = qts
        self.canceled = canceled
        self.payment_failed = payment_failed
        self.restored = restored

    @staticmethod
    def _parse(client: "pyrogram.Client", update: "raw.types.UpdateBotStarsSubscription") -> "BotStarsSubscription":
        return BotStarsSubscription(
            client=client,
            user_id=update.user_id,
            payload=update.payload,
            qts=update.qts,
            canceled=update.canceled,
            payment_failed=update.payment_failed,
            restored=update.restored,
        )
