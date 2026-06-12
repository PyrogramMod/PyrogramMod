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

from datetime import datetime
from typing import Dict

import pyrogram
from pyrogram import raw, utils
from pyrogram import types
from ..object import Object
from ..update import Update


class ChatJoinRequest(Object, Update):
    """Represents a join request sent to a chat.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`):
            Chat to which the request was sent.

        from_user (:obj:`~pyrogram.types.User`):
            User that sent the join request.

        date (:py:obj:`~datetime.datetime`):
            Date the request was sent.

        bio (``str``, *optional*):
            Bio of the user.

        invite_link (:obj:`~pyrogram.types.ChatInviteLink`, *optional*):
            Chat invite link that was used by the user to send the join request.

        query_id (``int``, *optional*):
            Guard-bot query ID. Present when the join request was routed through a guard bot.
            Pass to :meth:`~pyrogram.Client.answer_chat_join_request_query`.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        chat: "types.Chat",
        from_user: "types.User",
        date: datetime,
        bio: str = None,
        invite_link: "types.ChatInviteLink" = None,
        query_id: int = None,
    ):
        super().__init__(client)

        self.chat = chat
        self.from_user = from_user
        self.date = date
        self.bio = bio
        self.invite_link = invite_link
        self.query_id = query_id

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        update: "raw.types.UpdateBotChatInviteRequester",
        users: Dict[int, "raw.types.User"],
        chats: Dict[int, "raw.types.Chat"]
    ) -> "ChatJoinRequest":
        chat_id = utils.get_raw_peer_id(update.peer)

        return ChatJoinRequest(
            chat=types.Chat._parse_chat(client, chats[chat_id]),
            from_user=types.User._parse(client, users[update.user_id]),
            date=utils.timestamp_to_datetime(update.date),
            bio=update.about,
            invite_link=types.ChatInviteLink._parse(client, update.invite, users),
            query_id=getattr(update, "query_id", None),
            client=client
        )

    async def approve(self) -> bool:
        """Bound method *approve* of :obj:`~pyrogram.types.ChatJoinRequest`.
        
        Use as a shortcut for:
        
        .. code-block:: python

            await client.approve_chat_join_request(
                chat_id=request.chat.id,
                user_id=request.from_user.id
            )
            
        Example:
            .. code-block:: python

                await request.approve()
                
        Returns:
            ``bool``: True on success.
        
        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.approve_chat_join_request(
            chat_id=self.chat.id,
            user_id=self.from_user.id
        )

    async def decline(self) -> bool:
        """Bound method *decline* of :obj:`~pyrogram.types.ChatJoinRequest`.
        
        Use as a shortcut for:
        
        .. code-block:: python

            await client.decline_chat_join_request(
                chat_id=request.chat.id,
                user_id=request.from_user.id
            )
            
        Example:
            .. code-block:: python

                await request.decline()
                
        Returns:
            ``bool``: True on success.
        
        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.decline_chat_join_request(
            chat_id=self.chat.id,
            user_id=self.from_user.id
        )

    async def answer(self, action: str, url: str = None) -> None:
        """Answer this join request via the guard-bot query system.

        Requires :attr:`query_id` to be set (join request routed through a guard bot).

        Shortcut for :meth:`~pyrogram.Client.answer_chat_join_request_query`.

        Parameters:
            action (``str``):
                One of ``"approve"``, ``"decline"``, ``"queue"``, ``"web_view"``.

            url (``str``, *optional*):
                WebApp URL. Required when ``action="web_view"``.

        Raises:
            ValueError: If ``query_id`` is not set.
        """
        if self.query_id is None:
            raise ValueError("query_id is not set on this ChatJoinRequest")
        await self._client.answer_chat_join_request_query(self.query_id, action, url=url)

    async def answer_web_app(self, url: str) -> None:
        """Open a WebApp for the joining user via guard-bot query.

        Shortcut for :meth:`~pyrogram.Client.send_chat_join_request_web_app`.

        Parameters:
            url (``str``):
                HTTPS URL of the WebApp.
        """
        await self.answer("web_view", url=url)
