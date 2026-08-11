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


class CallbackAnswer(Object):
    """Bot callback answer.

    Parameters:
        message (``str``, *optional*):
            Alert message.

        alert (``bool``):
            True if an alert should be shown instead of a toast.

        has_url (``bool``):
            True if the answer contains a URL.

        url (``str``, *optional*):
            URL to open.

        cache_time (``int``):
            Time in seconds the answer should be cached.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        message: Optional[str] = None,
        alert: bool = False,
        has_url: bool = False,
        url: Optional[str] = None,
        cache_time: int = 0,
    ):
        super().__init__(client)
        self.message = message
        self.alert = alert
        self.has_url = has_url
        self.url = url
        self.cache_time = cache_time

    @staticmethod
    def _parse(client: "pyrogram.Client", raw_answer: "raw.base.messages.BotCallbackAnswer") -> "CallbackAnswer":
        return CallbackAnswer(
            client=client,
            message=getattr(raw_answer, "message", None),
            alert=getattr(raw_answer, "alert", False),
            has_url=getattr(raw_answer, "has_url", False),
            url=getattr(raw_answer, "url", None),
            cache_time=getattr(raw_answer, "cache_time", 0),
        )
