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


class DeleteGift:
    async def delete_gift(
        self: "pyrogram.Client",
        message_id: Optional[int] = None,
        chat_id: Optional[Union[int, str]] = None,
        saved_id: Optional[int] = None
    ) -> bool:
        """Delete a received gift.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            message_id (int, *optional*):
                Identifier of the service message of a gift received in a private chat.

            chat_id (int | str, *optional*):
                Unique identifier (int) or username (str) of the chat that owns the gift.
                Use together with saved_id.

            saved_id (int, *optional*):
                Saved identifier of a gift owned by a chat or channel.

        Returns:
            bool: True on success.

        Example:
            .. code-block:: python

                await app.delete_gift(message_id=123)
                await app.delete_gift(chat_id=-100123, saved_id=456)
        """
        if message_id is not None:
            gift = raw.types.InputSavedStarGiftUser(msg_id=message_id)
        elif chat_id is not None and saved_id is not None:
            gift = raw.types.InputSavedStarGiftChat(peer=await self.resolve_peer(chat_id), saved_id=saved_id)
        else:
            raise ValueError("Pass message_id, or both chat_id and saved_id")

        return await self.invoke(raw.functions.payments.DeleteStarGift(stargift=gift))
