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
from pyrogram import raw, enums
from ..object import Object


class RichButtonStyle(Object):
    """Visual style for a rich button.

    Parameters:
        bg_primary (``bool``, *optional*):
            Use primary background color.

        bg_danger (``bool``, *optional*):
            Use danger/red background color.

        bg_success (``bool``, *optional*):
            Use success/green background color.

        link (``bool``, *optional*):
            Render as a link-style button.
    """

    def __init__(
        self,
        bg_primary: bool = False,
        bg_danger: bool = False,
        bg_success: bool = False,
        link: bool = False,
    ):
        self.bg_primary = bg_primary
        self.bg_danger = bg_danger
        self.bg_success = bg_success
        self.link = link

    def write(self) -> "raw.types.RichButtonStyle":
        return raw.types.RichButtonStyle(
            bg_primary=self.bg_primary or None,
            bg_danger=self.bg_danger or None,
            bg_success=self.bg_success or None,
            link=self.link or None,
        )

    @staticmethod
    def _parse(raw_style: "raw.base.RichButtonStyle") -> "RichButtonStyle":
        return RichButtonStyle(
            bg_primary=getattr(raw_style, "bg_primary", False),
            bg_danger=getattr(raw_style, "bg_danger", False),
            bg_success=getattr(raw_style, "bg_success", False),
            link=getattr(raw_style, "link", False),
        )


class InlineButtonType(Object):
    """Type of action for an inline button in a rich message.

    Use the class methods to create specific button types:
    - :meth:`InlineButtonType.url`
    - :meth:`InlineButtonType.callback`
    - :meth:`InlineButtonType.web_view`
    - :meth:`InlineButtonType.buy`
    - :meth:`InlineButtonType.game`
    - :meth:`InlineButtonType.switch_inline`
    - :meth:`InlineButtonType.user_profile`
    - :meth:`InlineButtonType.copy`
    - :meth:`InlineButtonType.url_auth`
    - :meth:`InlineButtonType.disabled`

    Example:
        .. code-block:: python

            from pyrogram.types import InlineButtonType

            # URL button
            btn_type = InlineButtonType.url("https://pyrogram.org")

            # Callback button
            btn_type = InlineButtonType.callback(b"my_data")

            # Web view button
            btn_type = InlineButtonType.web_view("https://app.example.com")
    """

    def __init__(self, raw_type: "raw.base.InlineButtonType"):
        self._raw = raw_type

    def write(self) -> "raw.base.InlineButtonType":
        return self._raw

    @classmethod
    def url(cls, url: str) -> "InlineButtonType":
        """Open a URL."""
        return cls(raw.types.InlineButtonTypeUrl(url=url))

    @classmethod
    def callback(cls, data: bytes, requires_password: bool = False) -> "InlineButtonType":
        """Send callback data."""
        return cls(raw.types.InlineButtonTypeCallback(
            data=data,
            requires_password=requires_password or None,
        ))

    @classmethod
    def web_view(cls, url: str) -> "InlineButtonType":
        """Open a web view."""
        return cls(raw.types.InlineButtonTypeWebView(url=url))

    @classmethod
    def buy(cls) -> "InlineButtonType":
        """Buy button."""
        return cls(raw.types.InlineButtonTypeBuy())

    @classmethod
    def game(cls) -> "InlineButtonType":
        """Game button."""
        return cls(raw.types.InlineButtonTypeGame())

    @classmethod
    def switch_inline(
        cls,
        query: str,
        same_peer: bool = False,
        peer_types: "raw.base.InlineQueryPeerType" = None,
    ) -> "InlineButtonType":
        """Switch to inline mode."""
        return cls(raw.types.InlineButtonTypeSwitchInline(
            query=query,
            same_peer=same_peer or None,
            peer_types=peer_types,
        ))

    @classmethod
    def user_profile(cls, user_id: int) -> "InlineButtonType":
        """Open a user profile."""
        return cls(raw.types.InlineButtonTypeUserProfile(user_id=user_id))

    @classmethod
    def copy(cls, copy_text: str) -> "InlineButtonType":
        """Copy text to clipboard."""
        return cls(raw.types.InlineButtonTypeCopy(copy_text=copy_text))

    @classmethod
    def url_auth(
        cls,
        url: str,
        button_id: int,
        fwd_text: Optional[str] = None,
    ) -> "InlineButtonType":
        """URL with authorization."""
        return cls(raw.types.InlineButtonTypeUrlAuth(
            url=url,
            button_id=button_id,
            fwd_text=fwd_text,
        ))

    @classmethod
    def disabled(cls) -> "InlineButtonType":
        """Disabled button."""
        return cls(raw.types.InlineButtonTypeDisabled())

    @staticmethod
    def _parse(raw_type: "raw.base.InlineButtonType") -> "InlineButtonType":
        return InlineButtonType(raw_type)
