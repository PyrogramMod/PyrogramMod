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

from typing import Union

import pyrogram
from pyrogram import raw


class ToggleForum:
    async def toggle_forum(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        enabled: bool,
        tabs: bool = False,
        sidebar: bool = False
    ) -> bool:
        """Enable or disable topics (forum mode) in a supergroup.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target supergroup.

            enabled (``bool``):
                Pass True to enable forum mode, False to disable.

            tabs (``bool``, *optional*):
                Show the topics as tabs.

            sidebar (``bool``, *optional*):
                Show the topics in a sidebar (layer 233).

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.toggle_forum(chat_id, True, sidebar=True)
        """
        await self.invoke(
            raw.functions.channels.ToggleForum(
                channel=await self.resolve_peer(chat_id),
                enabled=enabled,
                tabs=tabs,
                sidebar=sidebar
            )
        )

        return True
