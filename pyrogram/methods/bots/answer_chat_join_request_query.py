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

from typing import Literal, Optional

import pyrogram
from pyrogram import raw

_ACTIONS = {"approve", "decline", "queue", "web_view"}


class AnswerChatJoinRequestQuery:
    async def answer_chat_join_request_query(
        self: "pyrogram.Client",
        query_id: int,
        action: Literal["approve", "decline", "queue", "web_view"],
        url: Optional[str] = None,
    ) -> bool:
        """Answer a chat join request query received via :obj:`~pyrogram.types.ChatJoinRequest`.

        When a chat uses a guard bot and a user requests to join, the guard bot
        receives a :obj:`~pyrogram.types.ChatJoinRequest` with a ``query_id``.
        The bot must call this method to act on the request.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            query_id (``int``):
                Unique identifier of the query (``ChatJoinRequest.query_id``).

            action (``str``):
                Decision for the join request. One of:

                - ``"approve"`` — approve the user immediately.
                - ``"decline"`` — reject the join request.
                - ``"queue"`` — hold the request for later review.
                - ``"web_view"`` — open a WebApp for the user (requires ``url``).

            url (``str``, *optional*):
                HTTPS URL of the WebApp to open.
                Required when ``action="web_view"``.

        Returns:
            ``bool``: True on success.

        Raises:
            ValueError: On unknown action or missing url for web_view.

        Example:
            .. code-block:: python

                @app.on_chat_join_request()
                async def handler(client, request):
                    if request.query_id:
                        await client.answer_chat_join_request_query(
                            request.query_id, "approve"
                        )
                    else:
                        await request.approve()
        """
        if action not in _ACTIONS:
            raise ValueError(f"Unknown action '{action}'. Valid: {', '.join(sorted(_ACTIONS))}")

        if action == "web_view":
            if not url:
                raise ValueError("url is required when action='web_view'")
            result = raw.types.JoinChatBotResultWebView(url=url)
        elif action == "approve":
            result = raw.types.JoinChatBotResultApproved()
        elif action == "decline":
            result = raw.types.JoinChatBotResultDeclined()
        else:
            result = raw.types.JoinChatBotResultQueued()

        return await self.invoke(
            raw.functions.bots.SetJoinChatResults(
                query_id=query_id,
                result=result,
            )
        )
