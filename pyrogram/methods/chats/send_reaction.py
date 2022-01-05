#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2022 Dan <https://github.com/delivrance>
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
from typing import Union

from pyrogram import raw
from pyrogram.scaffold import Scaffold


class SendReaction(Scaffold):
    async def send_reaction(
            self,
            chat_id: Union[int, str],
            msg_id: int,
            reaction: Union[str, None]
    ):
        """
            React to message with emoji

            Use :meth:`~pyrogram.Client.send_reaction` to react a message..

            Parameters:
                chat_id (``int`` | ``str``):
                    Unique identifier (int) or username (str) of the target chat.

                msg_id (``int``):
                    message_id to which you want to react

                reaction: Emoji (``str``):
                    Emoji to use for reaction

            Example:
                .. code-block:: python

                    app.send_reaction(chat_id, 123, "👍")
        """
        r = await self.send(
            raw.functions.messages.SendReaction(
                peer=await self.resolve_peer(chat_id),
                msg_id=msg_id,
                reaction=reaction,
            )
        )
        return getattr(r.updates[0], "message", r.updates[0]).reactions.results[0]
