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


class UpdateWebBrowserSettings:
    async def update_web_browser_settings(
        self: "pyrogram.Client",
        open_external_browser: Optional[bool] = None,
        display_close_button: Optional[bool] = None
    ) -> "raw.base.WebBrowserSettings":
        """Update the in-app web browser settings.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            open_external_browser (``bool``, *optional*):
                Pass True to open web links in external browser by default.

            display_close_button (``bool``, *optional*):
                Pass True to show the close button in the in-app browser.

        Returns:
            :obj:`~pyrogram.raw.types.WebBrowserSettings`: Updated settings.

        Example:
            .. code-block:: python

                await app.update_web_browser_settings(open_external_browser=True)
        """

        return await self.invoke(
            raw.functions.account.UpdateWebBrowserSettings(
                open_external_browser=open_external_browser,
                display_close_button=display_close_button
            )
        )
