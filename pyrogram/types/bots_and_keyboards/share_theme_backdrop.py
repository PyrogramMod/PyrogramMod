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


class ShareThemeBackdrop(Object):
    """A backdrop available for the chat link-sharing theme.

    Parameters:
        id (int):
            Unique identifier of the backdrop.

        name (str):
            Name of the backdrop.

        center_color (int):
            Center color of the backdrop, in RGB.

        edge_color (int):
            Edge color of the backdrop, in RGB.

        pattern_color (int):
            Color of the pattern, in RGB.

        text_color (int):
            Color of the text, in RGB.
    """

    def __init__(
        self, *,
        id: int,
        name: str,
        center_color: int,
        edge_color: int,
        pattern_color: int,
        text_color: int
    ):
        super().__init__()

        self.id = id
        self.name = name
        self.center_color = center_color
        self.edge_color = edge_color
        self.pattern_color = pattern_color
        self.text_color = text_color

    @staticmethod
    def _parse(option: "raw.types.ShareThemeBackdropOption") -> "ShareThemeBackdrop":
        return ShareThemeBackdrop(
            id=option.backdrop_id,
            name=option.name,
            center_color=option.center_color,
            edge_color=option.edge_color,
            pattern_color=option.pattern_color,
            text_color=option.text_color
        )
