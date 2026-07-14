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

import os
import re
from typing import BinaryIO, List, Union

import pyrogram
from pyrogram import raw, types, utils
from pyrogram.file_id import FileType


class SendStory:
    async def send_story(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        media: Union[str, BinaryIO],
        caption: str = None,
        period: int = 86400,
        pinned: bool = None,
        protect_content: bool = None,
        parse_mode: "pyrogram.enums.ParseMode" = None,
        caption_entities: List["types.MessageEntity"] = None,
        privacy_rules: List["raw.base.InputPrivacyRule"] = None
    ) -> "types.StoryItem":
        """Send a new story.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your own stories you can use "me" or "self".

            media (``str`` | ``BinaryIO``):
                Photo or video to send as story.
                Pass a file_id as string to send a file that exists on the Telegram servers,
                pass an HTTP URL as string for Telegram to get a file from the Internet,
                pass a file path as string to upload a new file from the local filesystem,
                or pass a binary file-like object to upload from memory.

            caption (``str``, *optional*):
                Story caption, 0-2048 characters.

            period (``int``, *optional*):
                Period after which the story will expire, in seconds.
                Default is 86400 (24 hours). Allowed values: 6*3600 (6 hours),
                12*3600 (12 hours), 86400 (24 hours), 2*86400 (48 hours).

            pinned (``bool``, *optional*):
                Whether to pin the story to the profile.

            protect_content (``bool``, *optional*):
                Protects the story from forwarding and saving.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using HTML style.
                Pass "markdown" or "md" to enable Markdown-style parsing.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                List of special entities that appear in the caption.

            privacy_rules (List of :obj:`~pyrogram.raw.base.InputPrivacyRule`, *optional*):
                Privacy rules for the story. If not provided, defaults to public.

        Returns:
            :obj:`~pyrogram.types.StoryItem`: On success, the sent story is returned.

        Example:
            .. code-block:: python

                # Send a photo story
                await app.send_story("me", "photo.jpg", caption="My story!")

                # Send a video story
                await app.send_story("me", "video.mp4")

                # Send a story with limited visibility
                from pyrogram import raw
                await app.send_story(
                    "me",
                    "photo.jpg",
                    privacy_rules=[raw.types.InputPrivacyValueAllowCloseFriends()]
                )
        """
        peer = await self.resolve_peer(chat_id)

        # Parse caption
        message, entities = (await utils.parse_text_entities(
            self, caption, parse_mode, caption_entities
        )).values()

        # Determine if it's a photo or video
        if isinstance(media, str):
            if os.path.isfile(media):
                # Local file
                file_name = os.path.basename(media)
                mime_type = self.guess_mime_type(media) or "application/octet-stream"

                if mime_type.startswith("video/"):
                    # Upload as video
                    media_obj = await self.invoke(
                        raw.functions.messages.UploadMedia(
                            peer=peer,
                            media=raw.types.InputMediaUploadedDocument(
                                file=await self.save_file(media),
                                mime_type=mime_type,
                                attributes=[
                                    raw.types.DocumentAttributeVideo(
                                        supports_streaming=True,
                                        duration=0,
                                        w=0,
                                        h=0
                                    ),
                                    raw.types.DocumentAttributeFilename(file_name=file_name)
                                ]
                            )
                        )
                    )
                    input_media = raw.types.InputMediaDocument(
                        id=raw.types.InputDocument(
                            id=media_obj.document.id,
                            access_hash=media_obj.document.access_hash,
                            file_reference=media_obj.document.file_reference
                        )
                    )
                else:
                    # Upload as photo
                    media_obj = await self.invoke(
                        raw.functions.messages.UploadMedia(
                            peer=peer,
                            media=raw.types.InputMediaUploadedPhoto(
                                file=await self.save_file(media)
                            )
                        )
                    )
                    input_media = raw.types.InputMediaPhoto(
                        id=raw.types.InputPhoto(
                            id=media_obj.photo.id,
                            access_hash=media_obj.photo.access_hash,
                            file_reference=media_obj.photo.file_reference
                        )
                    )
            elif re.match("^https?://", media):
                # URL
                if any(ext in media.lower() for ext in [".mp4", ".mov", ".avi", ".webm"]):
                    input_media = raw.types.InputMediaDocumentExternal(url=media)
                else:
                    input_media = raw.types.InputMediaPhotoExternal(url=media)
            else:
                # file_id
                decoded = utils.decode_file_id(media)
                if decoded.file_type == FileType.PHOTO:
                    input_media = raw.types.InputMediaPhoto(
                        id=raw.types.InputPhoto(
                            id=decoded.media_id,
                            access_hash=decoded.access_hash,
                            file_reference=decoded.file_reference
                        )
                    )
                else:
                    input_media = raw.types.InputMediaDocument(
                        id=raw.types.InputDocument(
                            id=decoded.media_id,
                            access_hash=decoded.access_hash,
                            file_reference=decoded.file_reference
                        )
                    )
        else:
            # BinaryIO - determine type from content
            mime_type = getattr(media, "mime_type", None) or "image/jpeg"
            if mime_type.startswith("video/"):
                media_obj = await self.invoke(
                    raw.functions.messages.UploadMedia(
                        peer=peer,
                        media=raw.types.InputMediaUploadedDocument(
                            file=await self.save_file(media),
                            mime_type=mime_type,
                            attributes=[
                                raw.types.DocumentAttributeVideo(
                                    supports_streaming=True,
                                    duration=0,
                                    w=0,
                                    h=0
                                )
                            ]
                        )
                    )
                )
                input_media = raw.types.InputMediaDocument(
                    id=raw.types.InputDocument(
                        id=media_obj.document.id,
                        access_hash=media_obj.document.access_hash,
                        file_reference=media_obj.document.file_reference
                    )
                )
            else:
                media_obj = await self.invoke(
                    raw.functions.messages.UploadMedia(
                        peer=peer,
                        media=raw.types.InputMediaUploadedPhoto(
                            file=await self.save_file(media)
                        )
                    )
                )
                input_media = raw.types.InputMediaPhoto(
                    id=raw.types.InputPhoto(
                        id=media_obj.photo.id,
                        access_hash=media_obj.photo.access_hash,
                        file_reference=media_obj.photo.file_reference
                    )
                )

        # Default privacy rules (public)
        if privacy_rules is None:
            privacy_rules = [raw.types.InputPrivacyValueAllowAll()]

        r = await self.invoke(
            raw.functions.stories.SendStory(
                peer=peer,
                media=input_media,
                caption=message,
                entities=entities,
                privacy_rules=privacy_rules,
                period=period,
                pinned=pinned,
                noforwards=protect_content
            )
        )

        users = {u.id: u for u in r.users}
        chats = {c.id: c for c in r.chats}

        for update in r.updates:
            if isinstance(update, raw.types.UpdateStory):
                if isinstance(update.story, raw.types.StoryItem):
                    return await types.StoryItem._parse(
                        self, update.story, users, chats, update.peer
                    )

        return None
