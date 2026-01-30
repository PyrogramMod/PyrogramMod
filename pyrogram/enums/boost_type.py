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

from .auto_name import AutoName


class BoostType(AutoName):
    """Boost type enumeration."""

    PREMIUM = "premium"
    """Boost from a Premium subscription."""

    GIFT = "gift"
    """Boost from a gift."""

    GIVEAWAY = "giveaway"
    """Boost from a giveaway."""

    STARS = "stars"
    """Boost from Telegram Stars."""
