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

from .handler import Handler


class GuardBotQueryHandler(Handler):
    """Handler for incoming guard bot queries.

    Triggered when a user requests to join a channel/supergroup that has
    this bot set as guard bot via :meth:`~pyrogram.Client.set_chat_guard_bot`.

    Register it with :meth:`~pyrogram.Client.add_handler` or use the
    :meth:`~pyrogram.Client.on_guard_bot_query` decorator.

    Parameters:
        callback (``Callable``):
            Function called when a :obj:`~pyrogram.types.GuardBotQuery` arrives.
            Takes *(client, guard_bot_query)* as positional arguments.

        filters (:obj:`~pyrogram.filters`, *optional*):
            Filters to restrict which queries trigger this handler.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself.

        guard_bot_query (:obj:`~pyrogram.types.GuardBotQuery`):
            The received guard bot query.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
