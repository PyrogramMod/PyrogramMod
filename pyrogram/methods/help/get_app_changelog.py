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


class GetAppChangelog:
    async def get_app_changelog(
        self: "pyrogram.Client",
        prev_app_version: str,
    ) -> "raw.base.Updates":
        """Get the app changelog for a specific previous app version.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            prev_app_version (``str``):
                The previous app version string (e.g. ``"4.0.0"``).

        Returns:
            :obj:`~pyrogram.raw.base.Updates`: The changelog updates.

        Example:
            .. code-block:: python

                changelog = await app.get_app_changelog("4.0.0")
        """
        return await self.invoke(
            raw.functions.help.GetAppChangelog(
                prev_app_version=prev_app_version
            )
        )
