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

from typing import Callable

import pyrogram
from pyrogram.filters import Filter


class OnGuardBotQuery:
    def on_guard_bot_query(
        self=None,
        filters=None,
        group: int = 0,
    ) -> Callable:
        """Decorator for handling guard bot queries.

        Triggered when a user requests to join a channel/supergroup protected
        by this guard bot. The bot must respond by calling one of the bound
        methods on :obj:`~pyrogram.types.GuardBotQuery` or by calling
        :meth:`~pyrogram.Client.answer_guard_bot_query` directly.

        This does the same thing as :meth:`~pyrogram.Client.add_handler` using
        :obj:`~pyrogram.handlers.GuardBotQueryHandler`.

        Parameters:
            filters (:obj:`~pyrogram.filters`, *optional*):
                Filters to restrict which queries trigger the handler.

            group (``int``, *optional*):
                Handler group. Defaults to 0.

        Example:
            .. code-block:: python

                @app.on_guard_bot_query()
                async def handle(client, query):
                    # approve everyone
                    await query.approve()

                @app.on_guard_bot_query()
                async def handle(client, query):
                    # open a captcha WebApp
                    await query.open_web_view("https://example.com/captcha")
        """

        def decorator(func: Callable) -> Callable:
            if isinstance(self, pyrogram.Client):
                self.add_handler(pyrogram.handlers.GuardBotQueryHandler(func, filters), group)
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append(
                    (
                        pyrogram.handlers.GuardBotQueryHandler(func, self),
                        group if filters is None else filters,
                    )
                )

            return func

        return decorator
