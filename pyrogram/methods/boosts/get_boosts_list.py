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

from typing import Union, List, AsyncGenerator, Optional

import pyrogram
from pyrogram import raw, types


class GetBoostsList:
    async def get_boosts_list(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        limit: int = 0,
        offset: str = ""
    ) -> AsyncGenerator["types.Boost", None]:
        """Get the list of boosts for a channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target channel.
                You can also use channel public link in form of *t.me/<username>* (str).

            limit (``int``, *optional*):
                Limits the number of boosts to be retrieved.
                By default, no limit is applied and all boosts are returned.

            offset (``str``, *optional*):
                Offset for pagination.

        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Boost` objects.

        Example:
            .. code-block:: python

                async for boost in app.get_boosts_list(chat_id):
                    print(boost.user)
        """
        peer = await self.resolve_peer(chat_id)
        current = 0
        total = abs(limit) or (1 << 31) - 1
        limit = min(100, total)

        while True:
            r: raw.types.premium.BoostsList = await self.invoke(
                raw.functions.premium.GetBoostsList(
                    peer=peer,
                    offset=offset,
                    limit=limit
                )
            )

            users = {u.id: u for u in r.users}

            boosts = types.Boost._parse_list(self, r.boosts, users)

            if not boosts:
                return

            for boost in boosts:
                yield boost

                current += 1

                if current >= total:
                    return

            offset = r.next_offset

            if not offset:
                return
