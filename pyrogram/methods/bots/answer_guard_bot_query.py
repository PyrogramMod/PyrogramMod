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

from typing import Optional, Literal

import pyrogram
from pyrogram import raw

_ACTIONS = {"approve", "decline", "queue", "web_view"}


class AnswerGuardBotQuery:
    async def answer_guard_bot_query(
        self: "pyrogram.Client",
        query_id: int,
        action: Literal["approve", "decline", "queue", "web_view"],
        url: Optional[str] = None,
    ) -> None:
        """Answer a guard bot query received via :obj:`~pyrogram.types.GuardBotQuery`.

        Guard bots receive :obj:`~pyrogram.types.GuardBotQuery` updates when a user
        requests to join a channel/supergroup protected by the bot. Every query
        must be answered.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            query_id (``int``):
                Unique identifier of the query to answer.

            action (``str``):
                Decision for the join request. One of:

                - ``"approve"`` — approve the user immediately.
                - ``"decline"`` — reject the join request.
                - ``"queue"`` — hold the request for later review.
                - ``"web_view"`` — open a WebApp for the user (requires ``url``).

            url (``str``, *optional*):
                HTTPS URL of the WebApp to open for the user.
                Required when ``action="web_view"``.

        Raises:
            ValueError: On unknown action or missing url for web_view.

        Example:
            .. code-block:: python

                # Approve
                await app.answer_guard_bot_query(query.query_id, "approve")

                # Decline
                await app.answer_guard_bot_query(query.query_id, "decline")

                # Show captcha WebApp
                await app.answer_guard_bot_query(
                    query.query_id,
                    "web_view",
                    url="https://example.com/captcha"
                )
        """

        if action not in _ACTIONS:
            raise ValueError(f"Unknown action '{action}'. Valid: {', '.join(_ACTIONS)}")

        if action == "web_view":
            if not url:
                raise ValueError("url is required when action='web_view'")
            send_message = raw.types.InputBotInlineMessageText(message=url)
        else:
            send_message = raw.types.InputBotInlineMessageText(message="")

        await self.invoke(
            raw.functions.messages.SetBotGuestChatResult(
                query_id=query_id,
                result=raw.types.InputBotInlineResult(
                    id=action,
                    type=action,
                    send_message=send_message,
                ),
            )
        )
