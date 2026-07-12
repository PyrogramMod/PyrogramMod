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


class AddChatToCommunity:
    async def add_chat_to_community(
        self: "pyrogram.Client",
        community_id: Union[int, str],
        chat_id: Union[int, str],
        hidden: bool = False,
    ) -> bool:
        """Add a chat to an existing community.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            community_id (``int`` | ``str``):
                The community channel to add the chat to.

            chat_id (``int`` | ``str``):
                The chat to add.

            hidden (``bool``, *optional*):
                Pass True to add the chat as hidden (not visible in the community sidebar).
                Defaults to False (visible).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Add visible
                await app.add_chat_to_community(-1001966997491, chat_id)

                # Add hidden
                await app.add_chat_to_community(-1001966997491, chat_id, hidden=True)
        """

        community = await self.resolve_peer(community_id)
        peer = await self.resolve_peer(chat_id)

        await self.invoke(
            raw.functions.communities.TogglePeerLink(
                community=community,
                peer=peer,
                visible=True if not hidden else None,
                hidden=True if hidden else None,
            )
        )

        return True
