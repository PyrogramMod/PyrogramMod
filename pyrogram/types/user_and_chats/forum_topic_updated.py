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

from typing import Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object
from ..update import Update


class ForumTopicUpdated(Object, Update):
    """A forum topic was edited. Only the fields that changed are set.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            The forum.

        topic_id (``int``):
            Identifier of the topic (the id of its first message).

        title (``str``, *optional*):
            New title.

        icon_emoji_id (``int``, *optional*):
            New custom emoji identifier of the icon. 0 means the icon was removed.

        is_closed (``bool``, *optional*):
            True, if the topic was closed, False if reopened.

        is_hidden (``bool``, *optional*):
            True, if the topic was hidden, False if shown.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        chat: "types.Chat" = None,
        topic_id: int,
        title: Optional[str] = None,
        icon_emoji_id: Optional[int] = None,
        is_closed: Optional[bool] = None,
        is_hidden: Optional[bool] = None
    ):
        super().__init__(client)

        self.chat = chat
        self.topic_id = topic_id
        self.title = title
        self.icon_emoji_id = icon_emoji_id
        self.is_closed = is_closed
        self.is_hidden = is_hidden

    @staticmethod
    def _parse(client, update: "raw.types.UpdateEditForumTopic", users, chats) -> "ForumTopicUpdated":
        return ForumTopicUpdated(
            chat=utils.parse_peer_chat(client, update.peer, users, chats),
            topic_id=update.topic_id,
            title=update.title,
            icon_emoji_id=update.icon_emoji_id,
            is_closed=update.closed,
            is_hidden=update.hidden,
            client=client
        )
