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


class BusinessIntro(Object):
    """Represents a business introduction message shown to new contacts.

    Parameters:
        title (``str``, *optional*):
            Title of the introduction.

        description (``str``, *optional*):
            Description text of the introduction.

        sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
            Sticker shown in the introduction.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        title: str = None,
        description: str = None,
        sticker: "types.Sticker" = None
    ):
        super().__init__(client)

        self.title = title
        self.description = description
        self.sticker = sticker

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        intro: "raw.types.BusinessIntro"
    ) -> Optional["BusinessIntro"]:
        if intro is None:
            return None

        sticker = None
        if intro.sticker:
            sticker = await types.Sticker._parse(client, intro.sticker, {})

        return BusinessIntro(
            client=client,
            title=intro.title,
            description=intro.description,
            sticker=sticker
        )
