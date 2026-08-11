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
from pyrogram import types
from ..object import Object


class WebViewResult(Object):
    """Result of a web view interaction.

    Parameters:
        url (``str``, *optional*):
            The web view URL.

        title (``str``, *optional*):
            Title of the result.

        description (``str``, *optional*):
            Description of the result.

        users (List of :obj:`~pyrogram.types.User`):
            List of users associated with the result.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        url: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        users: Optional[List["types.User"]] = None,
    ):
        super().__init__(client)
        self.url = url
        self.title = title
        self.description = description
        self.users = users or []

    @staticmethod
    def _parse(client: "pyrogram.Client", raw_result: "raw.base.messages.WebViewResult") -> "WebViewResult":
        result = raw_result.result
        users = [types.User._parse(client, u) for u in raw_result.users]

        return WebViewResult(
            client=client,
            url=getattr(result, "url", None),
            title=getattr(result, "title", None),
            description=getattr(result, "description", None),
            users=users,
        )
