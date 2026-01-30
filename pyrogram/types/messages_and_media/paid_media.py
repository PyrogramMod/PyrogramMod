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

from typing import List, Optional, Any

import pyrogram
from pyrogram import raw, types
from ..object import Object


class PaidMedia(Object):
    """Represents a paid media.

    Parameters:
        stars_amount (``int``):
            The amount of stars required to buy the media.

        extended_media (List of ``Any``, *optional*):
            List of extended media (preview or actual media).
            Can contain Photo, Video, or preview information.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        stars_amount: int,
        extended_media: List[Any] = None
    ):
        super().__init__(client)

        self.stars_amount = stars_amount
        self.extended_media = extended_media

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        paid_media: "raw.types.MessageMediaPaidMedia",
        users: dict = None,
        chats: dict = None
    ) -> Optional["PaidMedia"]:
        if not paid_media:
            return None

        users = users or {}
        chats = chats or {}

        extended_media = []
        if paid_media.extended_media:
            for ext_media in paid_media.extended_media:
                if isinstance(ext_media, raw.types.MessageExtendedMedia):
                    media = ext_media.media

                    if isinstance(media, raw.types.MessageMediaPhoto):
                        parsed = types.Photo._parse(client, media.photo, media.ttl_seconds)
                        extended_media.append(parsed)
                    elif isinstance(media, raw.types.MessageMediaDocument):
                        doc = media.document
                        if isinstance(doc, raw.types.Document):
                            attributes = {type(i): i for i in doc.attributes}
                            file_name = getattr(
                                attributes.get(raw.types.DocumentAttributeFilename, None),
                                "file_name",
                                None
                            )
                            if raw.types.DocumentAttributeVideo in attributes:
                                video_attributes = attributes[raw.types.DocumentAttributeVideo]
                                parsed = types.Video._parse(client, doc, video_attributes, file_name, media.ttl_seconds)
                                extended_media.append(parsed)
                            else:
                                parsed = types.Document._parse(client, doc, file_name)
                                extended_media.append(parsed)
                elif isinstance(ext_media, raw.types.MessageExtendedMediaPreview):
                    preview_info = {
                        "type": "preview",
                        "w": ext_media.w if hasattr(ext_media, 'w') else None,
                        "h": ext_media.h if hasattr(ext_media, 'h') else None,
                        "video_duration": ext_media.video_duration if hasattr(ext_media, 'video_duration') else None
                    }
                    extended_media.append(preview_info)

        return PaidMedia(
            client=client,
            stars_amount=paid_media.stars_amount,
            extended_media=extended_media if extended_media else None
        )
