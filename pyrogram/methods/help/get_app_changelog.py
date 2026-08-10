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

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetAppChangelog:
    async def get_app_changelog(
        self: "pyrogram.Client",
        prev_app_version: str,
    ) -> "types.List":
        """Get the app changelog for a specific previous app version.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            prev_app_version (``str``):
                The previous app version string (e.g. ``"4.0.0"``).

        Returns:
            :obj:`~pyrogram.types.List` of :obj:`~pyrogram.types.Message`: The changelog messages.

        Example:
            .. code-block:: python

                changelog = await app.get_app_changelog("4.0.0")
                for msg in changelog:
                    print(msg.text)
        """
        r = await self.invoke(
            raw.functions.help.GetAppChangelog(
                prev_app_version=prev_app_version
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        messages = types.List()

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                              raw.types.UpdateNewChannelMessage)):
                messages.append(
                    await types.Message._parse(
                        self, i.message, users, chats
                    )
                )

        return messages
