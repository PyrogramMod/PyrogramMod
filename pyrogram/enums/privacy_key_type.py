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


class PrivacyKeyType(AutoName):
    """Privacy key type enumeration."""

    STATUS_TIMESTAMP = "status_timestamp"
    """Privacy for last seen timestamp."""

    CHAT_INVITE = "chat_invite"
    """Privacy for group/channel invitations."""

    PHONE_CALL = "phone_call"
    """Privacy for voice/video calls."""

    PHONE_P2P = "phone_p2p"
    """Privacy for P2P calls."""

    FORWARDS = "forwards"
    """Privacy for forwarded messages."""

    PROFILE_PHOTO = "profile_photo"
    """Privacy for profile photo."""

    PHONE_NUMBER = "phone_number"
    """Privacy for phone number."""

    ADDED_BY_PHONE = "added_by_phone"
    """Privacy for being added by phone number."""

    VOICE_MESSAGES = "voice_messages"
    """Privacy for voice messages."""

    ABOUT = "about"
    """Privacy for bio/about."""

    BIRTHDAY = "birthday"
    """Privacy for birthday."""

    GIFTS = "gifts"
    """Privacy for star gifts."""

    STARREF_LINKS = "starref_links"
    """Privacy for star referral links."""

    NO_PAID_MESSAGES = "no_paid_messages"
    """Privacy for receiving paid messages."""

    SAVED_MUSIC = "saved_music"
    """Privacy for who can see your saved music."""
