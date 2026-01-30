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
from pyrogram import raw, types
from ..object import Object


class MessageEffect(Object):
    """Represents a message effect.

    Parameters:
        id (``int``):
            Unique identifier of the effect.

        emoticon (``str``, *optional*):
            Emoticon associated with the effect.

        static_icon (:obj:`~pyrogram.types.Document`, *optional*):
            Static icon for the effect.

        effect_sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
            Animated sticker for the effect.

        effect_animation (:obj:`~pyrogram.types.Document`, *optional*):
            Animation for the effect.

        is_premium_required (``bool``, *optional*):
            Whether this effect requires Premium.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int = None,
        emoticon: str = None,
        static_icon: "types.Document" = None,
        effect_sticker: "types.Sticker" = None,
        effect_animation: "types.Document" = None,
        is_premium_required: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.emoticon = emoticon
        self.static_icon = static_icon
        self.effect_sticker = effect_sticker
        self.effect_animation = effect_animation
        self.is_premium_required = is_premium_required

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        effect: "raw.types.AvailableEffect"
    ) -> "MessageEffect":
        static_icon = None
        effect_sticker = None
        effect_animation = None

        if hasattr(effect, 'static_icon_id') and effect.static_icon_id:
            # Would need to fetch the document
            pass

        if hasattr(effect, 'effect_sticker_id') and effect.effect_sticker_id:
            # Would need to fetch the sticker
            pass

        if hasattr(effect, 'effect_animation_id') and effect.effect_animation_id:
            # Would need to fetch the animation
            pass

        return MessageEffect(
            client=client,
            id=effect.id,
            emoticon=effect.emoticon if hasattr(effect, 'emoticon') else None,
            static_icon=static_icon,
            effect_sticker=effect_sticker,
            effect_animation=effect_animation,
            is_premium_required=effect.premium_required if hasattr(effect, 'premium_required') else None
        )
