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
from pyrogram import raw, types
from ..object import Object


class BusinessChatLink(Object):
    """Represents a business chat link.

    Parameters:
        link (``str``):
            The link.

        message (``str``):
            The message associated with the link.

        views (``int``):
            Number of views.

        title (``str``, *optional*):
            Title of the link.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            List of special entities that appear in the message.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        link: str,
        message: str,
        views: int,
        title: str = None,
        entities: List["types.MessageEntity"] = None
    ):
        super().__init__(client)

        self.link = link
        self.message = message
        self.views = views
        self.title = title
        self.entities = entities

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        link: "raw.types.BusinessChatLink"
    ) -> "BusinessChatLink":
        return BusinessChatLink(
            client=client,
            link=link.link,
            message=link.message,
            views=link.views,
            title=link.title,
            entities=types.List([
                types.MessageEntity._parse(client, entity, {})
                for entity in link.entities
            ]) if link.entities else None
        )

    @property
    def slug(self) -> str:
        """The slug of the business chat link."""
        return self.link.split("/")[-1]

    async def edit(
        self,
        message: str = None,
        title: str = None,
        entities: List["types.MessageEntity"] = None
    ) -> "BusinessChatLink":
        """Bound method *edit* of :obj:`~pyrogram.types.BusinessChatLink`.

        Use as a shortcut for:
            .. code-block:: python

                await link.edit(message="New message")

        Parameters:
            message (``str``, *optional*):
                The new message associated with the link.

            title (``str``, *optional*):
                The new title of the link.

            entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                List of special entities that appear in the message.

        Returns:
            :obj:`~pyrogram.types.BusinessChatLink`: On success, the edited business chat link is returned.
        """
        return await self._client.edit_business_chat_link(
            slug=self.slug,
            link=raw.types.InputBusinessChatLink(
                message=message or self.message,
                title=title or self.title,
                entities=entities or self.entities
            )
        )

    async def delete(self) -> bool:
        """Bound method *delete* of :obj:`~pyrogram.types.BusinessChatLink`.

        Use as a shortcut for:
            .. code-block:: python

                await link.delete()

        Returns:
            ``bool``: True on success.
        """
        return await self._client.delete_business_chat_link(slug=self.slug)
