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
from pyrogram import raw, types

class SendStoryReaction:
    async def send_story_reaction(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_id: int,
        reaction: "types.Reaction" = None,
        add_to_recent: bool = None
    ) -> bool:
        """Send a reaction to a story.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            story_id (``int``):
                The story ID.

            reaction (:obj:`~pyrogram.types.Reaction`, *optional*):
                The reaction to send. If not provided, it will remove the existing reaction.

            add_to_recent (``bool``, *optional*):
                Whether to add the reaction to the recent reactions list.

        Returns:
            ``bool``: True on success.
        """
        rpc = raw.functions.stories.SendReaction(
            peer=await self.resolve_peer(chat_id),
            story_id=story_id,
            reaction=await reaction.write(self) if reaction else raw.types.ReactionEmpty(),
            add_to_recent=add_to_recent
        )
        return await self.invoke(rpc)
