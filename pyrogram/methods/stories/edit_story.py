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

from typing import List, Union

import pyrogram
from pyrogram import raw, types, utils


class EditStory:
    async def edit_story(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_id: int,
        caption: str = None,
        parse_mode: "pyrogram.enums.ParseMode" = None,
        caption_entities: List["types.MessageEntity"] = None,
        privacy_rules: List["raw.base.InputPrivacyRule"] = None
    ) -> "types.StoryItem":
        """Edit a story.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your own stories you can use "me" or "self".

            story_id (``int``):
                The ID of the story to edit.

            caption (``str``, *optional*):
                New caption for the story, 0-2048 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using HTML style.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                List of special entities that appear in the new caption.

            privacy_rules (List of :obj:`~pyrogram.raw.base.InputPrivacyRule`, *optional*):
                New privacy rules for the story.

        Returns:
            :obj:`~pyrogram.types.StoryItem`: On success, the edited story is returned.

        Example:
            .. code-block:: python

                # Edit story caption
                await app.edit_story("me", 12345, caption="Updated caption!")
        """
        peer = await self.resolve_peer(chat_id)

        # Parse caption
        message = None
        entities = None
        if caption is not None:
            parsed = await utils.parse_text_entities(
                self, caption, parse_mode, caption_entities
            )
            message = parsed.get("message")
            entities = parsed.get("entities")

        r = await self.invoke(
            raw.functions.stories.EditStory(
                peer=peer,
                id=story_id,
                caption=message,
                entities=entities,
                privacy_rules=privacy_rules
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
