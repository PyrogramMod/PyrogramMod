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


class BotVerifierSettings(Object):
    """Bot verifier settings.

    Parameters:
        icon (``int``):
            The custom emoji ID used as a verification icon.

        company (``str``):
            The company name.

        can_modify_custom_description (``bool``, *optional*):
            Whether the bot can modify the custom description.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        icon: int,
        company: str,
        can_modify_custom_description: bool = None
    ):
        super().__init__(client)

        self.icon = icon
        self.company = company
        self.can_modify_custom_description = can_modify_custom_description

    @staticmethod
    def _parse(client: "pyrogram.Client", settings: "raw.types.BotVerifierSettings") -> "BotVerifierSettings":
        if not settings:
            return None

        return BotVerifierSettings(
            client=client,
            icon=settings.icon,
            company=settings.company,
            can_modify_custom_description=getattr(settings, "can_modify_custom_description", None)
        )
