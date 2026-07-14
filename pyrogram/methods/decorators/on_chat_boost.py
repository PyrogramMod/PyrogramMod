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

import pyrogram
from pyrogram.handlers import ChatBoostHandler


class OnChatBoost:
    def on_chat_boost(
        self,
        filters=None,
        group: int = 0
    ) -> callable:
        """Decorator for handling chat boost updates.

        Parameters:
            filters (:obj:`~pyrogram.filters`, *optional*):
                Pass one or more filters to speculate on which updates to handle.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """
        def decorator(func: callable) -> callable:
            if isinstance(self, pyrogram.Client):
                self.add_handler(ChatBoostHandler(func, filters), group)

            return func

        return decorator
