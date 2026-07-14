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


class PollLink(Object):
    """A link attached to a poll option as its media.

    Parameters:
        url (``str``):
            Full URL.

        display_url (``str``, *optional*):
            Display URL shown to users.

        title (``str``, *optional*):
            Link title.

        description (``str``, *optional*):
            Link description.

        photo (:obj:`~pyrogram.types.Photo`, *optional*):
            Preview photo, if available.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        url: str,
        display_url: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        photo: Optional["types.Photo"] = None,
    ):
        super().__init__(client)
        self.url = url
        self.display_url = display_url
        self.title = title
        self.description = description
        self.photo = photo

    @staticmethod
    def _parse(client: "pyrogram.Client", media: "raw.base.MessageMedia") -> Optional["PollLink"]:
        if not isinstance(media, raw.types.MessageMediaWebPage):
            return None
        wp = media.webpage
        if not isinstance(wp, raw.types.WebPage):
            return None
        return PollLink(
            client=client,
            url=wp.url,
            display_url=wp.display_url,
            title=getattr(wp, "title", None),
            description=getattr(wp, "description", None),
            photo=types.Photo._parse(client, wp.photo, None) if getattr(wp, "photo", None) else None,
        )
