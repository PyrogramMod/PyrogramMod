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

from typing import Optional, List

import pyrogram
from pyrogram import raw, types
from ..object import Object


class FactCheck(Object):
    """Represents a fact check attached to a message.

    Parameters:
        text (``str``):
            The fact check text.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Special entities in the fact check text (links, formatting, etc.).

        country (``str``, *optional*):
            The country code where the fact check applies.

        hash (``int``, *optional*):
            Hash for caching.

        need_check (``bool``, *optional*):
            Whether the message needs a fact check.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        text: str = None,
        entities: List["types.MessageEntity"] = None,
        country: str = None,
        hash: int = None,
        need_check: bool = None
    ):
        super().__init__(client)

        self.text = text
        self.entities = entities
        self.country = country
        self.hash = hash
        self.need_check = need_check

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        factcheck: "raw.types.FactCheck"
    ) -> Optional["FactCheck"]:
        if factcheck is None:
            return None

        entities = None
        if hasattr(factcheck, 'text') and factcheck.text:
            text = factcheck.text.text if hasattr(factcheck.text, 'text') else str(factcheck.text)
            if hasattr(factcheck.text, 'entities') and factcheck.text.entities:
                entities = [
                    types.MessageEntity._parse(client, e, {})
                    for e in factcheck.text.entities
                ]
        else:
            text = None

        return FactCheck(
            client=client,
            text=text,
            entities=types.List(entities) if entities else None,
            country=factcheck.country if hasattr(factcheck, 'country') else None,
            hash=factcheck.hash if hasattr(factcheck, 'hash') else None,
            need_check=factcheck.need_check if hasattr(factcheck, 'need_check') else None
        )
