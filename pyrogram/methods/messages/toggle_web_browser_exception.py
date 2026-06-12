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


class ToggleWebBrowserException:
    async def toggle_web_browser_exception(
        self: "pyrogram.Client",
        url: str,
        open_external_browser: Optional[bool] = None,
        delete: bool = False
    ) -> bool:
        """Add or remove a domain exception for the in-app web browser.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            url (``str``):
                The URL or domain to add/remove as exception.

            open_external_browser (``bool``, *optional*):
                Pass True to open this domain in external browser, False to open in-app.
                Ignored if ``delete`` is True.

            delete (``bool``, *optional*):
                Pass True to remove the exception for this URL. Defaults to False.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Add exception: open in external browser
                await app.toggle_web_browser_exception("https://example.com", open_external_browser=True)

                # Remove exception
                await app.toggle_web_browser_exception("https://example.com", delete=True)
        """

        await self.invoke(
            raw.functions.account.ToggleWebBrowserSettingsException(
                url=url,
                open_external_browser=open_external_browser,
                delete=delete
            )
        )

        return True
