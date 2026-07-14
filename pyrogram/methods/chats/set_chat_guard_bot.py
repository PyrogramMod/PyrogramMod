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


class SetChatGuardBot:
    async def set_chat_guard_bot(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        bot: Optional[Union[int, str]] = None,
        apply_to_invites: bool = False
    ) -> bool:
        """Set or remove a guard bot for a channel or supergroup.

        The guard bot screens join requests before approval.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            bot (``int`` | ``str`` | ``None``):
                Unique identifier (int) or username (str) of the bot to set as guard.
                Pass ``None`` to remove the guard bot (disables join request screening).

            apply_to_invites (``bool``, *optional*):
                Pass True to also apply guard bot screening to invite link joins.
                Defaults to False.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                # Set a guard bot
                await app.set_chat_guard_bot(chat_id, "@myguardbot")

                # Set guard bot and apply to invite links too
                await app.set_chat_guard_bot(chat_id, "@myguardbot", apply_to_invites=True)

                # Remove guard bot
                await app.set_chat_guard_bot(chat_id, None)
        """

        guard_bot = None
        if bot is not None:
            peer = await self.resolve_peer(bot)
            if isinstance(peer, raw.types.InputPeerUser):
                guard_bot = raw.types.InputUser(user_id=peer.user_id, access_hash=peer.access_hash)
            else:
                guard_bot = peer

        await self.invoke(
            raw.functions.channels.ToggleJoinRequest(
                channel=await self.resolve_peer(chat_id),
                enabled=guard_bot is not None,
                guard_bot=guard_bot,
                apply_to_invites=apply_to_invites
            )
        )

        return True
