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
            community_id (``int``):
                The raw community ID (as returned by ``linked_community_id`` on
                :obj:`~pyrogram.types.Chat` or by :meth:`~pyrogram.Client.get_joined_communities`).
                Note: this is **not** the ``-100``-prefixed channel ID.

            chat_id (``int`` | ``str``):
                The chat or peer to add to the community.

            hidden (``bool``, *optional*):
                Pass True to add the chat as hidden (not visible in the community sidebar).
                Defaults to False (visible).

        Returns:
            ``bool``: True on success.

        Raises:
            ~pyrogram.errors.PeerLinkNotModified: The chat is already linked
                to the community.
            ~pyrogram.errors.ChatAdminRequired: The user is not an admin of
                the community or the chat.

        Example:
            .. code-block:: python

                # Get the community ID from a linked chat
                chat = await app.get_chat(my_channel_id)
                community_id = chat.linked_community_id

                # Add visible
                await app.add_chat_to_community(community_id, chat_id)

                # Add hidden
                await app.add_chat_to_community(community_id, chat_id, hidden=True)
        """

        # Community objects have raw IDs (no -100 prefix) and are not in the
        # peer cache, so resolve_peer can't handle them. Fetch the access_hash
        # from the joined-communities list instead.
        if isinstance(community_id, int):
            r = await self.invoke(raw.functions.communities.GetJoinedCommunities())
            target_id = abs(community_id)
            match = next((c for c in r.chats if c.id == target_id), None)
            if match is None:
                raise ValueError(f"Community {community_id} not found in joined communities")
            community = raw.types.InputChannel(
                channel_id=match.id,
                access_hash=match.access_hash,
            )
        else:
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
