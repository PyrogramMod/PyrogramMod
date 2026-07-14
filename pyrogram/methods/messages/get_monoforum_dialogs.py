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


class GetMonoforumDialogs:
    async def get_monoforum_dialogs(
        self: "pyrogram.Client",
        channel_id: Union[int, str],
        limit: int = 0,
    ) -> "raw.base.messages.SavedDialogs":
        """Get the list of per-sender sublists (dialogs) of a monoforum channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            channel_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the monoforum channel.

            limit (``int``, *optional*):
                Limits the number of dialogs to be retrieved. Defaults to 100.

        Returns:
            :obj:`~pyrogram.raw.base.messages.SavedDialogs`: The raw dialogs list.

        Example:
            .. code-block:: python

                dialogs = await app.get_monoforum_dialogs(channel_id)
        """
        parent_peer = await self.resolve_peer(channel_id)

        return await self.invoke(
            raw.functions.messages.GetSavedDialogs(
                parent_peer=parent_peer,
                offset_date=0,
                offset_id=0,
                offset_peer=raw.types.InputPeerEmpty(),
                limit=limit or 100,
                hash=0
            )
        )
