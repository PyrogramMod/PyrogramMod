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

from typing import Dict, List, Optional

import pyrogram
from pyrogram import raw, types, enums
from ..object import Object
from ..update import Update


class GuardBotQuery(Object, Update):
    """Incoming guard bot query sent by Telegram when a user requests to join a chat.

    The guard bot receives this update and must respond with
    :meth:`~pyrogram.Client.answer_guard_bot_query` or the bound methods
    :meth:`~pyrogram.types.GuardBotQuery.approve`, :meth:`~pyrogram.types.GuardBotQuery.decline`,
    :meth:`~pyrogram.types.GuardBotQuery.queue`, or :meth:`~pyrogram.types.GuardBotQuery.open_web_view`.

    Parameters:
        query_id (``int``):
            Unique identifier for this query. Pass to :meth:`~pyrogram.Client.answer_guard_bot_query`.

        message (:obj:`~pyrogram.types.Message`):
            The join-request message that triggered this query.

        qts (``int``):
            QTS value for state synchronisation.

        reference_messages (List of :obj:`~pyrogram.types.Message`, *optional*):
            Additional context messages provided by Telegram.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        query_id: int,
        message: "types.Message",
        qts: int,
        reference_messages: Optional[List["types.Message"]] = None,
    ):
        super().__init__(client)

        self.query_id = query_id
        self.message = message
        self.qts = qts
        self.reference_messages = reference_messages

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        update: "raw.types.UpdateBotGuestChatQuery",
        users: Dict[int, "raw.base.User"],
        chats: Dict[int, "raw.base.Chat"],
    ) -> "GuardBotQuery":
        ref_messages = None
        if update.reference_messages:
            ref_messages = [
                await types.Message._parse(client, m, users, chats)
                for m in update.reference_messages
            ]

        return GuardBotQuery(
            query_id=update.query_id,
            message=await types.Message._parse(client, update.message, users, chats),
            qts=update.qts,
            reference_messages=ref_messages,
            client=client,
        )

    async def approve(self) -> None:
        """Approve the join request.

        Shortcut for :meth:`~pyrogram.Client.answer_guard_bot_query` with ``action="approve"``.

        Example:
            .. code-block:: python

                @app.on_guard_bot_query()
                async def handler(client, query):
                    await query.approve()
        """
        await self._client.answer_guard_bot_query(self.query_id, "approve")

    async def decline(self) -> None:
        """Decline the join request.

        Shortcut for :meth:`~pyrogram.Client.answer_guard_bot_query` with ``action="decline"``.

        Example:
            .. code-block:: python

                @app.on_guard_bot_query()
                async def handler(client, query):
                    await query.decline()
        """
        await self._client.answer_guard_bot_query(self.query_id, "decline")

    async def queue(self) -> None:
        """Put the join request in the queue (hold for later review).

        Shortcut for :meth:`~pyrogram.Client.answer_guard_bot_query` with ``action="queue"``.

        Example:
            .. code-block:: python

                @app.on_guard_bot_query()
                async def handler(client, query):
                    await query.queue()
        """
        await self._client.answer_guard_bot_query(self.query_id, "queue")

    async def open_web_view(self, url: str) -> None:
        """Present a WebApp to the joining user.

        Shortcut for :meth:`~pyrogram.Client.answer_guard_bot_query` with ``action="web_view"``.

        Parameters:
            url (``str``):
                HTTPS URL of the WebApp to open for the user.

        Example:
            .. code-block:: python

                @app.on_guard_bot_query()
                async def handler(client, query):
                    await query.open_web_view("https://example.com/captcha")
        """
        await self._client.answer_guard_bot_query(self.query_id, "web_view", url=url)
