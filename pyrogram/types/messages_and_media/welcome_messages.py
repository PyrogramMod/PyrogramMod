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

from typing import List

import pyrogram
from pyrogram import raw
from ..object import Object


class WelcomeMessages(Object):
    """Welcome messages configured for a chat.

    Parameters:
        hash (``int``):
            Hash for caching.

        messages (List of :obj:`~pyrogram.raw.base.EphemeralMessage`):
            List of ephemeral welcome messages.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        hash: int,
        messages: List["raw.base.EphemeralMessage"],
    ):
        super().__init__(client)
        self.hash = hash
        self.messages = messages

    @staticmethod
    def _parse(client: "pyrogram.Client", raw_welcome: "raw.base.WelcomeMessages") -> "WelcomeMessages":
        if isinstance(raw_welcome, raw.types.WelcomeMessagesNotModified):
            return WelcomeMessages(client=client, hash=0, messages=[])

        return WelcomeMessages(
            client=client,
            hash=raw_welcome.hash,
            messages=raw_welcome.messages,
        )
