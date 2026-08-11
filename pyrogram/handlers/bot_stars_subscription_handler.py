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


class BotStarsSubscriptionHandler(Handler):
    """The BotStarsSubscription handler class. Used to handle bot stars subscription updates.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the
    :meth:`~pyrogram.Client.on_bot_stars_subscription` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new bot stars subscription update arrives.
            It takes *(client, bot_stars_subscription)* as positional arguments.

        filters (:obj:`Filters`):
            Pass one or more filters to allow only a subset of updates to be passed.

    Other parameters:
        client (:obj:`~pyrogram.Client`):
            The Client itself.

        bot_stars_subscription (:obj:`~pyrogram.types.BotStarsSubscription`):
            The bot stars subscription update.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
