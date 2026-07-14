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

import pyrogram
from pyrogram import raw
from ..object import Object


class InputRichMessage(Object):
    """A rich message to send.

    Pass an instance of this class to :meth:`~pyrogram.Client.send_rich_message` or
    :meth:`~pyrogram.Client.send_rich_message_draft`.

    Parameters:
        blocks (List of ``raw.base.PageBlock``):
            Content blocks. Use raw ``pyrogram.raw.types.PageBlock*`` constructors directly.

        rtl (``bool``, *optional*):
            Pass True for right-to-left content.

        noautolink (``bool``, *optional*):
            Pass True to disable automatic link detection.

    Example:
        .. code-block:: python

            from pyrogram.raw import types as raw_types
            from pyrogram.types import InputRichMessage

            msg = InputRichMessage(blocks=[
                raw_types.PageBlockParagraph(
                    text=raw_types.TextPlain(text="Hello, rich world!")
                ),
                raw_types.PageBlockPreformatted(
                    text=raw_types.TextPlain(text="print('hi')"),
                    language="python"
                ),
            ])
            await app.send_rich_message(chat_id, msg)
    """

    def __init__(
        self,
        *,
        blocks: List["raw.base.PageBlock"],
        rtl: bool = False,
        noautolink: bool = False,
    ):
        super().__init__(None)
        self.blocks = blocks
        self.rtl = rtl
        self.noautolink = noautolink

    def write(self) -> "raw.types.InputRichMessage":
        return raw.types.InputRichMessage(
            blocks=self.blocks,
            rtl=self.rtl or None,
            noautolink=self.noautolink or None,
        )
