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

from typing import Optional

import pyrogram
from pyrogram import raw, types
from ..object import Object


class PaidReactionPrivacy(Object):
    """Paid reaction privacy settings.

    Parameters:
        type (``str``):
            The type of privacy setting. Can be "default", "anonymous" or "peer".

        peer (:obj:`~pyrogram.types.Chat`, *optional*):
            The peer to send reactions as. Only available if type is "peer".
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        type: str,
        peer: "types.Chat" = None
    ):
        super().__init__(client)

        self.type = type
        self.peer = peer

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        privacy: "raw.base.PaidReactionPrivacy",
        chats: dict = None
    ) -> "PaidReactionPrivacy":
        chats = chats or {}

        if isinstance(privacy, raw.types.PaidReactionPrivacyDefault):
            return PaidReactionPrivacy(client=client, type="default")

        if isinstance(privacy, raw.types.PaidReactionPrivacyAnonymous):
            return PaidReactionPrivacy(client=client, type="anonymous")

        if isinstance(privacy, raw.types.PaidReactionPrivacyPeer):
            # We can't fully parse the peer here without resolving input peer
            # but we can try our best or just indicate it's a peer type
            return PaidReactionPrivacy(
                client=client,
                type="peer"
            )

        return None
