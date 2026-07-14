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


class SuggestedPost(Object):
    """Represents a suggested post for a channel.

    Parameters:
        schedule_date (:py:obj:`~datetime.datetime`, *optional*):
            Scheduled date for the post.

        price (``int``, *optional*):
            Price in Telegram Stars for the suggested post.

        is_pending (``bool``, *optional*):
            Whether the post is pending approval.

        is_rejected (``bool``, *optional*):
            Whether the post was rejected.

        is_accepted (``bool``, *optional*):
            Whether the post was accepted.

        rejection_reason (``str``, *optional*):
            Reason for rejection if rejected.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        schedule_date: datetime = None,
        price: int = None,
        is_pending: bool = None,
        is_rejected: bool = None,
        is_accepted: bool = None,
        rejection_reason: str = None
    ):
        super().__init__(client)

        self.schedule_date = schedule_date
        self.price = price
        self.is_pending = is_pending
        self.is_rejected = is_rejected
        self.is_accepted = is_accepted
        self.rejection_reason = rejection_reason

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        suggested_post: "raw.types.SuggestedPost"
    ) -> Optional["SuggestedPost"]:
        if suggested_post is None:
            return None

        return SuggestedPost(
            client=client,
            schedule_date=utils.timestamp_to_datetime(suggested_post.schedule_date) if hasattr(suggested_post, 'schedule_date') and suggested_post.schedule_date else None,
            price=suggested_post.price if hasattr(suggested_post, 'price') else None,
            is_pending=suggested_post.pending if hasattr(suggested_post, 'pending') else None,
            is_rejected=suggested_post.rejected if hasattr(suggested_post, 'rejected') else None,
            is_accepted=suggested_post.accepted if hasattr(suggested_post, 'accepted') else None,
            rejection_reason=suggested_post.rejection_reason if hasattr(suggested_post, 'rejection_reason') else None
        )
