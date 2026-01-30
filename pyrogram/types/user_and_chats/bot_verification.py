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


class BotVerification(Object):
    """Represents bot verification information.

    Parameters:
        bot_id (``int``):
            The ID of the verification bot.

        icon (``int``):
            Custom emoji ID for the verification icon.

        description (``str``, *optional*):
            Description of the verification.
    """

    def __init__(
        self,
        *,
        bot_id: int = None,
        icon: int = None,
        description: str = None
    ):
        super().__init__()

        self.bot_id = bot_id
        self.icon = icon
        self.description = description

    @staticmethod
    def _parse(verification: "raw.types.BotVerification") -> Optional["BotVerification"]:
        if verification is None:
            return None

        return BotVerification(
            bot_id=verification.bot_id,
            icon=verification.icon,
            description=verification.description if hasattr(verification, 'description') else None
        )
