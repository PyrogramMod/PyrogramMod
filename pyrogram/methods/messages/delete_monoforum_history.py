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


class DeleteMonoforumHistory:
    async def delete_monoforum_history(
        self: "pyrogram.Client",
        channel_id: Union[int, str],
        peer_id: Union[int, str],
        max_id: int = 0,
    ) -> bool:
        """Delete a monoforum sender sublist's message history.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            channel_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the monoforum channel.

            peer_id (``int`` | ``str``):
                Unique identifier of the sender whose sublist to delete.

            max_id (``int``, *optional*):
                The id of the last message to delete. Defaults to 0 (delete the whole history).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_monoforum_history(channel_id, peer_id)
        """
        await self.invoke(
            raw.functions.messages.DeleteSavedHistory(
                parent_peer=await self.resolve_peer(channel_id),
                peer=await self.resolve_peer(peer_id),
                max_id=max_id
            )
        )

        return True
