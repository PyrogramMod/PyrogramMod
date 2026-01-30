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


class StoryPrivacyType(AutoName):
    """Story privacy type enumeration."""

    PUBLIC = "public"
    """Story visible to everyone."""

    CONTACTS = "contacts"
    """Story visible to contacts only."""

    CLOSE_FRIENDS = "close_friends"
    """Story visible to close friends only."""

    SELECTED = "selected"
    """Story visible to selected users only."""
