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


class RichMessage(Object):
    """A rich formatted message.

    Parameters:
        blocks (List of :obj:`~pyrogram.types.RichBlock`):
            Content blocks.

        rtl (``bool``, *optional*):
            True if the message is right-to-left.

        is_partial (``bool``, *optional*):
            True if this is a partial/streaming update rather than the final message.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        blocks: List["pyrogram.types.RichBlock"],
        rtl: bool = False,
        is_partial: bool = False,
    ):
        super().__init__(client)
        self.blocks = blocks
        self.rtl = rtl
        self.is_partial = is_partial

    @staticmethod
    def _parse(client: "pyrogram.Client", raw_msg: "raw.types.RichMessage") -> Optional["RichMessage"]:
        if raw_msg is None:
            return None

        from .rich_block import RichBlock

        return RichMessage(
            client=client,
            blocks=[RichBlock._parse(client, b) for b in raw_msg.blocks],
            rtl=raw_msg.rtl or False,
            is_partial=raw_msg.part or False,
        )
