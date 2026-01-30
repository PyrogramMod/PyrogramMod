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

from datetime import datetime
from typing import List, Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class StickerSet(Object):
    """A sticker set.

    Parameters:
        id (``int``):
            Sticker set identifier.

        access_hash (``int``):
            Sticker set access hash.

        title (``str``):
            Sticker set title.

        short_name (``str``):
            Sticker set short name.

        count (``int``):
            Number of stickers in this set.

        hash (``int``):
            Sticker set hash.

        is_archived (``bool``, *optional*):
            True, if this sticker set is archived.

        is_official (``bool``, *optional*):
            True, if this sticker set is official.

        is_masks (``bool``, *optional*):
            True, if this sticker set contains masks.

        is_emojis (``bool``, *optional*):
            True, if this sticker set contains emojis.

        is_text_color (``bool``, *optional*):
            True, if this sticker set contains custom text color emojis.

        is_channel_emoji_status (``bool``, *optional*):
            True, if this sticker set contains custom channel status emojis.

        is_creator (``bool``, *optional*):
            True, if you created this sticker set.

        installed_date (``datetime``, *optional*):
            Date when the sticker set was installed.

        thumbs (List of :obj:`~pyrogram.types.Thumbnail`, *optional*):
            Sticker set thumbnails.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        access_hash: int,
        title: str,
        short_name: str,
        count: int,
        hash: int,
        is_archived: bool = None,
        is_official: bool = None,
        is_masks: bool = None,
        is_emojis: bool = None,
        is_text_color: bool = None,
        is_channel_emoji_status: bool = None,
        is_creator: bool = None,
        installed_date: datetime = None,
        thumbs: List["types.Thumbnail"] = None
    ):
        super().__init__(client)

        self.id = id
        self.access_hash = access_hash
        self.title = title
        self.short_name = short_name
        self.count = count
        self.hash = hash
        self.is_archived = is_archived
        self.is_official = is_official
        self.is_masks = is_masks
        self.is_emojis = is_emojis
        self.is_text_color = is_text_color
        self.is_channel_emoji_status = is_channel_emoji_status
        self.is_creator = is_creator
        self.installed_date = installed_date
        self.thumbs = thumbs

    @staticmethod
    def _parse(client: "pyrogram.Client", sticker_set: "raw.types.StickerSet") -> "StickerSet":
        if not sticker_set:
            return None

        return StickerSet(
            client=client,
            id=sticker_set.id,
            access_hash=sticker_set.access_hash,
            title=sticker_set.title,
            short_name=sticker_set.short_name,
            count=sticker_set.count,
            hash=sticker_set.hash,
            is_archived=getattr(sticker_set, "archived", None),
            is_official=getattr(sticker_set, "official", None),
            is_masks=getattr(sticker_set, "masks", None),
            is_emojis=getattr(sticker_set, "emojis", None),
            is_text_color=getattr(sticker_set, "text_color", None),
            is_channel_emoji_status=getattr(sticker_set, "channel_emoji_status", None),
            is_creator=getattr(sticker_set, "creator", None),
            installed_date=utils.timestamp_to_datetime(getattr(sticker_set, "installed_date", None)),
            thumbs=types.Thumbnail._parse(client, sticker_set)
        )
