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

import pyrogram
from pyrogram import raw
from ..object import Object


class StarRefProgram(Object):
    """A Telegram Stars affiliate program.

    Parameters:
        commission_per_mille (``int``):
            Commission in per mille (1/1000).

        duration_months (``int``, *optional*):
            Duration of the program in months.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        commission_per_mille: int,
        duration_months: int = None
    ):
        super().__init__(client)

        self.commission_per_mille = commission_per_mille
        self.duration_months = duration_months

    @staticmethod
    def _parse(client: "pyrogram.Client", program: "raw.types.StarRefProgram") -> "StarRefProgram":
        if not program:
            return None

        return StarRefProgram(
            client=client,
            commission_per_mille=program.commission_per_mille,
            duration_months=getattr(program, "duration_months", None)
        )
