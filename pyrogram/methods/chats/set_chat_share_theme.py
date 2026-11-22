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

from typing import Union, Optional, List

import pyrogram
from pyrogram import raw


class SetChatShareTheme:
    async def set_chat_share_theme(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        backdrop_id: Optional[int] = None,
        emojis: Optional[List[str]] = None
    ) -> bool:
        """Set the theme shown on the link-sharing screen of a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (int | str):
                Unique identifier (int) or username (str) of the target chat.

            backdrop_id (int, *optional*):
                Identifier of the backdrop, see :meth:`~pyrogram.Client.get_share_theme_backdrops`.
                Pass None together with emojis=None to restore the default theme.

            emojis (List of str, *optional*):
                Emojis used in the backdrop pattern.

        Returns:
            bool: True on success.

        Example:
            .. code-block:: python

                await app.set_chat_share_theme(chat_id, backdrop_id=1, emojis=["🔥"])
        """
        if backdrop_id is None and not emojis:
            theme = raw.types.ShareThemeDefault()
        else:
            theme = raw.types.ShareThemeEmojiBackdrop(
                backdrop_id=backdrop_id,
                emojis=[raw.types.ReactionEmoji(emoticon=e) for e in emojis] if emojis else None
            )

        return await self.invoke(
            raw.functions.messages.SetShareTheme(
                peer=await self.resolve_peer(chat_id),
                theme=theme
            )
        )
