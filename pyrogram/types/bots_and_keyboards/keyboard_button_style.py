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

from pyrogram import raw
from ..object import Object


class KeyboardButtonStyle(Object):
    """Style configuration for keyboard buttons.

    Parameters:
        bg_primary (``bool``, *optional*):
            Use primary background color for the button.

        bg_danger (``bool``, *optional*):
            Use danger/red background color for the button.

        bg_success (``bool``, *optional*):
            Use success/green background color for the button.

        icon (``int``, *optional*):
            Custom emoji ID to use as button icon.
    """

    def __init__(
        self,
        *,
        bg_primary: bool = None,
        bg_danger: bool = None,
        bg_success: bool = None,
        icon: int = None
    ):
        super().__init__()

        self.bg_primary = bg_primary
        self.bg_danger = bg_danger
        self.bg_success = bg_success
        self.icon = icon

    @staticmethod
    def read(style: "raw.types.KeyboardButtonStyle") -> "KeyboardButtonStyle":
        if style is None:
            return None

        return KeyboardButtonStyle(
            bg_primary=style.bg_primary or None,
            bg_danger=style.bg_danger or None,
            bg_success=style.bg_success or None,
            icon=style.icon
        )

    def write(self) -> "raw.types.KeyboardButtonStyle":
        return raw.types.KeyboardButtonStyle(
            bg_primary=self.bg_primary,
            bg_danger=self.bg_danger,
            bg_success=self.bg_success,
            icon=self.icon
        )
