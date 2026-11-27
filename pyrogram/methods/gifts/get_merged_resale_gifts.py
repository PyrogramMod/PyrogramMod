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

from typing import List, Optional

import pyrogram
from pyrogram import raw


class GetMergedResaleGifts:
    async def get_merged_resale_gifts(
        self: "pyrogram.Client",
        gift_ids: List[int],
        offset: str = "",
        limit: int = 50,
        query: Optional[str] = None,
        sort_by_price: bool = None,
        sort_by_number: bool = None,
        sort_descending: bool = None,
        stars_only: bool = None,
        ton_only: bool = None,
        attributes: List["raw.base.StarGiftAttributeId"] = None,
        attributes_hash: Optional[int] = None
    ) -> "raw.types.payments.ResaleStarGifts":
        """Get collectible gifts on sale for several gift types in one list.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            gift_ids (List of ``int``):
                Identifiers of the base gifts to list.

            offset (``str``, *optional*):
                ``next_offset`` of the previous result, to get the next page.

            limit (``int``, *optional*):
                Maximum number of gifts to return.

            query (``str``, *optional*):
                Text to search for.

            sort_by_price (``bool``, *optional*):
                Sort by price instead of by date.

            sort_by_number (``bool``, *optional*):
                Sort by collectible number.

            sort_descending (``bool``, *optional*):
                Reverse the sort order.

            stars_only (``bool``, *optional*):
                Only gifts sold for Stars.

            ton_only (``bool``, *optional*):
                Only gifts sold for TON.

            attributes (List of :obj:`~pyrogram.raw.base.StarGiftAttributeId`, *optional*):
                Raw attributes to filter by.

            attributes_hash (``int``, *optional*):
                Hash of the attribute list you already have.

        Returns:
            :obj:`~pyrogram.raw.types.payments.ResaleStarGifts`: The raw gifts with ``next_offset``, chats and users.
            No high-level resale type exists yet.

        Example:
            .. code-block:: python

                r = await app.get_merged_resale_gifts([gift_id_1, gift_id_2], sort_by_price=True)
                for gift in r.gifts:
                    print(gift.title, gift.num)
        """
        return await self.invoke(
            raw.functions.payments.GetResaleStarGiftsMerged(
                gift_ids=gift_ids,
                offset=offset,
                limit=limit,
                query=query,
                sort_by_price=sort_by_price,
                sort_by_num=sort_by_number,
                sort_desc=sort_descending,
                stars_only=stars_only,
                ton_only=ton_only,
                attributes=attributes,
                attributes_hash=attributes_hash
            )
        )
