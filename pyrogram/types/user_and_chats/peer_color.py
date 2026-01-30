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

from typing import List, Optional

from pyrogram import raw
from ..object import Object


class PeerColor(Object):
    """Represents the accent color information of a peer.

    Parameters:
        color (``int``, *optional*):
            Identifier of the color palette.

        background_emoji_id (``int``, *optional*):
            Custom emoji identifier used for the background pattern.

        collectible_id (``int``, *optional*):
            Collectible identifier when the color comes from a collectible.

        gift_emoji_id (``int``, *optional*):
            Emoji identifier of the collectible gift.

        accent_color (``int``, *optional*):
            Accent color value for collectible colors.

        colors (List of ``int``, *optional*):
            List of palette colors for collectible colors.

        dark_accent_color (``int``, *optional*):
            Accent color for dark mode.

        dark_colors (List of ``int``, *optional*):
            Dark palette colors.
    """

    def __init__(
        self,
        *,
        client=None,
        color: Optional[int] = None,
        background_emoji_id: Optional[int] = None,
        collectible_id: Optional[int] = None,
        gift_emoji_id: Optional[int] = None,
        accent_color: Optional[int] = None,
        colors: Optional[List[int]] = None,
        dark_accent_color: Optional[int] = None,
        dark_colors: Optional[List[int]] = None
    ):
        super().__init__(client)

        self.color = color
        self.background_emoji_id = background_emoji_id
        self.collectible_id = collectible_id
        self.gift_emoji_id = gift_emoji_id
        self.accent_color = accent_color
        self.colors = colors
        self.dark_accent_color = dark_accent_color
        self.dark_colors = dark_colors

    @staticmethod
    def _parse(peer_color: "raw.base.PeerColor") -> Optional["PeerColor"]:
        if peer_color is None:
            return None

        if isinstance(peer_color, raw.types.PeerColor):
            return PeerColor(
                color=getattr(peer_color, "color", None),
                background_emoji_id=getattr(peer_color, "background_emoji_id", None)
            )

        if isinstance(peer_color, raw.types.PeerColorCollectible):
            return PeerColor(
                collectible_id=peer_color.collectible_id,
                gift_emoji_id=peer_color.gift_emoji_id,
                background_emoji_id=peer_color.background_emoji_id,
                accent_color=peer_color.accent_color,
                colors=list(peer_color.colors) if getattr(peer_color, "colors", None) else None,
                dark_accent_color=getattr(peer_color, "dark_accent_color", None),
                dark_colors=list(peer_color.dark_colors) if getattr(peer_color, "dark_colors", None) else None
            )

        return None
