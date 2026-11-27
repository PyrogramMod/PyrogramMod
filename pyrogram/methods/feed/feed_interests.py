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

from typing import List

import pyrogram
from pyrogram import raw


class FeedInterests:
    async def get_feed_interest_categories(
        self: "pyrogram.Client",
        hash: int = 0
    ) -> "raw.base.feed.InterestCategories":
        """Get the interest categories of the feed and the ones you selected.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            hash (``int``, *optional*):
                Hash of the list you already have.

        Returns:
            :obj:`~pyrogram.raw.base.feed.InterestCategories`: The raw categories and the selected ids.

        Example:
            .. code-block:: python

                r = await app.get_feed_interest_categories()
                for c in r.categories:
                    print(c.id, c.title)
        """
        return await self.invoke(raw.functions.feed.GetInterestCategories(hash=hash))

    async def set_feed_interest_categories(
        self: "pyrogram.Client",
        category_ids: List[int]
    ) -> bool:
        """Choose the interest categories of the feed.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            category_ids (List of ``int``):
                Identifiers of the chosen categories. Pass an empty list to clear them.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.set_feed_interest_categories([1, 4])
        """
        return await self.invoke(raw.functions.feed.SetInterestCategories(category_ids=category_ids))
