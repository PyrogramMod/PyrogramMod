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


class Wallpaper(Object):
    """Represents a wallpaper.

    Parameters:
        id (``int``):
            Unique wallpaper identifier.

        access_hash (``int``):
            Access hash.

        slug (``str``):
            Wallpaper slug/identifier.

        document (:obj:`~pyrogram.types.Document`, *optional*):
            The wallpaper document.

        settings (:obj:`~pyrogram.types.WallpaperSettings`, *optional*):
            Wallpaper settings.

        is_creator (``bool``, *optional*):
            Whether the current user created this wallpaper.

        is_default (``bool``, *optional*):
            Whether this is the default wallpaper.

        is_pattern (``bool``, *optional*):
            Whether this is a pattern wallpaper.

        is_dark (``bool``, *optional*):
            Whether this wallpaper is for dark mode.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int = None,
        access_hash: int = None,
        slug: str = None,
        document: "types.Document" = None,
        settings: "types.WallpaperSettings" = None,
        is_creator: bool = None,
        is_default: bool = None,
        is_pattern: bool = None,
        is_dark: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.access_hash = access_hash
        self.slug = slug
        self.document = document
        self.settings = settings
        self.is_creator = is_creator
        self.is_default = is_default
        self.is_pattern = is_pattern
        self.is_dark = is_dark

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        wallpaper: "raw.types.WallPaper"
    ) -> "Wallpaper":
        document = None
        if hasattr(wallpaper, 'document') and wallpaper.document:
            document = await types.Document._parse(client, wallpaper.document, "wallpaper.jpg")

        settings = None
        if hasattr(wallpaper, 'settings') and wallpaper.settings:
            settings = types.WallpaperSettings._parse(wallpaper.settings)

        return Wallpaper(
            client=client,
            id=wallpaper.id,
            access_hash=wallpaper.access_hash if hasattr(wallpaper, 'access_hash') else None,
            slug=wallpaper.slug,
            document=document,
            settings=settings,
            is_creator=wallpaper.creator if hasattr(wallpaper, 'creator') else None,
            is_default=wallpaper.default if hasattr(wallpaper, 'default') else None,
            is_pattern=wallpaper.pattern if hasattr(wallpaper, 'pattern') else None,
            is_dark=wallpaper.dark if hasattr(wallpaper, 'dark') else None
        )


class WallpaperSettings(Object):
    """Represents wallpaper settings.

    Parameters:
        background_color (``int``, *optional*):
            Background color in RGB format.

        second_background_color (``int``, *optional*):
            Second background color for gradients.

        third_background_color (``int``, *optional*):
            Third background color.

        fourth_background_color (``int``, *optional*):
            Fourth background color.

        intensity (``int``, *optional*):
            Pattern intensity (0-100).

        rotation (``int``, *optional*):
            Gradient rotation angle.

        emoticon (``str``, *optional*):
            Emoticon-based wallpaper.

        is_blur (``bool``, *optional*):
            Whether blur is applied.

        is_motion (``bool``, *optional*):
            Whether motion effects are enabled.
    """

    def __init__(
        self,
        *,
        background_color: int = None,
        second_background_color: int = None,
        third_background_color: int = None,
        fourth_background_color: int = None,
        intensity: int = None,
        rotation: int = None,
        emoticon: str = None,
        is_blur: bool = None,
        is_motion: bool = None
    ):
        super().__init__()

        self.background_color = background_color
        self.second_background_color = second_background_color
        self.third_background_color = third_background_color
        self.fourth_background_color = fourth_background_color
        self.intensity = intensity
        self.rotation = rotation
        self.emoticon = emoticon
        self.is_blur = is_blur
        self.is_motion = is_motion

    @staticmethod
    def _parse(settings: "raw.types.WallPaperSettings") -> Optional["WallpaperSettings"]:
        if settings is None:
            return None

        return WallpaperSettings(
            background_color=settings.background_color if hasattr(settings, 'background_color') else None,
            second_background_color=settings.second_background_color if hasattr(settings, 'second_background_color') else None,
            third_background_color=settings.third_background_color if hasattr(settings, 'third_background_color') else None,
            fourth_background_color=settings.fourth_background_color if hasattr(settings, 'fourth_background_color') else None,
            intensity=settings.intensity if hasattr(settings, 'intensity') else None,
            rotation=settings.rotation if hasattr(settings, 'rotation') else None,
            emoticon=settings.emoticon if hasattr(settings, 'emoticon') else None,
            is_blur=settings.blur if hasattr(settings, 'blur') else None,
            is_motion=settings.motion if hasattr(settings, 'motion') else None
        )
