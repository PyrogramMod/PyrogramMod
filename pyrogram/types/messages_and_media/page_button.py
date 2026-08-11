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


class PageButton(Object):
    """A button inside a rich message page block.

    Parameters:
        text (:obj:`~pyrogram.types.RichText`):
            Button label text.

        type (:obj:`~pyrogram.types.InlineButtonType`):
            Action performed when the button is pressed.

        style (:obj:`~pyrogram.types.RichButtonStyle`, *optional*):
            Visual style for the button.

    Example:
        .. code-block:: python

            from pyrogram.types import PageButton, RichText, InlineButtonType, RichButtonStyle

            button = PageButton(
                text=RichText(type=RichTextType.PLAIN, plain_text="Open Website"),
                type=InlineButtonType.url("https://pyrogram.org"),
                style=RichButtonStyle(bg_primary=True),
            )
    """

    def __init__(
        self,
        *,
        text: "pyrogram.types.RichText",
        type: "InlineButtonType",
        style: Optional["RichButtonStyle"] = None,
    ):
        super().__init__(None)
        self.text = text
        self.type = type
        self.style = style

    def write(self) -> "raw.types.PageButton":
        return raw.types.PageButton(
            text=self.text.write() if hasattr(self.text, 'write') else self.text,
            type=self.type.write(),
            style=self.style.write() if self.style else None,
        )

    @staticmethod
    def _parse(client: "pyrogram.Client", raw_button: "raw.types.PageButton") -> "PageButton":
        from .rich_text import RichText
        from .inline_button_type import InlineButtonType, RichButtonStyle

        return PageButton(
            text=RichText._parse(client, raw_button.text),
            type=InlineButtonType._parse(raw_button.type),
            style=RichButtonStyle._parse(raw_button.style) if raw_button.style else None,
        )
