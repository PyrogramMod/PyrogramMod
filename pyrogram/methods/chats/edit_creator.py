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

from typing import Union, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class EditCreator:
    async def edit_creator(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str],
        password: str,
    ) -> Optional["types.Message"]:
        """Transfer channel ownership to another user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target channel.

            user_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the user that will become the new creator.

            password (``str``):
                Your 2FA password (required for ownership transfer).

        Returns:
            :obj:`~pyrogram.types.Message` | ``None``: On success, the service message
            confirming the ownership transfer is returned, otherwise None.

        Example:
            .. code-block:: python

                await app.edit_creator(chat_id, user_id, "my_password")
        """
        r = await self.invoke(
            raw.functions.channels.EditCreator(
                channel=await self.resolve_peer(chat_id),
                user_id=await self.resolve_peer(user_id),
                password=raw.types.InputCheckPasswordSRP(
                    srp_id=0,
                    A=b"",
                    M1=b"",
                ),
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                              raw.types.UpdateNewChannelMessage)):
                return await types.Message._parse(
                    self, i.message, users, chats
                )

        return None
