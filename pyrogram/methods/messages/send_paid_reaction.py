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

from typing import Union

import pyrogram
from pyrogram import raw


class SendPaidReaction:
    async def send_paid_reaction(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int = None,
        count: int= None,
        private: bool= None,
    ) -> bool:
        """Send a reaction to a message.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the message.

            count (``int``)
                Number of reactions to send. Defaults to 1.

            private (``bool``)
                Whether the reaction should be private. Defaults to False.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Send paid reaction
                app.send_reaction_paid(chat_id=123456789, message_id=123, count=5, private=False)

                # Send private paid reaction
                app.send_reaction_paid(chat_id=123456789, message_id=123, count=5, private=True)

                # Retract paid reaction
                app.send_reaction_paid(chat_id=123456789, message_id=123, count=0)
        """

        if message_id is not None:
            await self.invoke(
                raw.functions.messages.SendPaidReaction(
                    peer=await self.resolve_peer(chat_id),
                    msg_id=message_id,
                    count=count,
                    private=private,
                    random_id=self.rnd_id()
                )
            )
        else:
            raise ValueError("You need to pass one of message_id!")
        return True
