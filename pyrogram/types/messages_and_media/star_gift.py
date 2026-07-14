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
from typing import Optional

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class StarGift(Object):
    """A star gift.

    Parameters:
        id (``int``):
            Unique identifier of the gift.

        sticker (:obj:`~pyrogram.types.Sticker`):
            Sticker that represents the gift.

        stars (``int``):
            Price of the gift in Telegram Stars.

        convert_stars (``int``):
            Amount of Stars the receiver can convert this gift to.

        limited (``bool``, *optional*):
            Whether this is a limited-supply gift.

        sold_out (``bool``, *optional*):
            Whether this gift sold out and cannot be bought anymore.

        birthday (``bool``, *optional*):
            Whether this is a birthday-themed gift.

        can_upgrade (``bool``, *optional*):
            Whether this gift can be upgraded to a collectible.

        require_premium (``bool``, *optional*):
            Whether this gift can only be bought by Premium users.

        availability_remains (``int``, *optional*):
            For limited-supply gifts: remaining number of gifts available.

        availability_total (``int``, *optional*):
            For limited-supply gifts: total number of gifts in initial supply.

        first_sale_date (:py:obj:`~datetime.datetime`, *optional*):
            For sold out gifts: when the gift was first bought.

        last_sale_date (:py:obj:`~datetime.datetime`, *optional*):
            For sold out gifts: when the gift was last bought.

        upgrade_stars (``int``, *optional*):
            Stars needed to upgrade this gift to a collectible.

        title (``str``, *optional*):
            Title of the gift.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        sticker: "types.Sticker" = None,
        stars: int,
        convert_stars: int,
        limited: bool = None,
        sold_out: bool = None,
        birthday: bool = None,
        can_upgrade: bool = None,
        require_premium: bool = None,
        availability_remains: int = None,
        availability_total: int = None,
        first_sale_date: datetime = None,
        last_sale_date: datetime = None,
        upgrade_stars: int = None,
        title: str = None
    ):
        super().__init__(client)

        self.id = id
        self.sticker = sticker
        self.stars = stars
        self.convert_stars = convert_stars
        self.limited = limited
        self.sold_out = sold_out
        self.birthday = birthday
        self.can_upgrade = can_upgrade
        self.require_premium = require_premium
        self.availability_remains = availability_remains
        self.availability_total = availability_total
        self.first_sale_date = first_sale_date
        self.last_sale_date = last_sale_date
        self.upgrade_stars = upgrade_stars
        self.title = title

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        star_gift: "raw.types.StarGift"
    ) -> "StarGift":
        return StarGift(
            client=client,
            id=star_gift.id,
            sticker=await types.Sticker._parse(client, star_gift.sticker, {}) if star_gift.sticker else None,
            stars=star_gift.stars,
            convert_stars=star_gift.convert_stars,
            limited=star_gift.limited or None,
            sold_out=star_gift.sold_out or None,
            birthday=star_gift.birthday or None,
            can_upgrade=star_gift.can_upgrade or None,
            require_premium=star_gift.require_premium or None,
            availability_remains=star_gift.availability_remains,
            availability_total=star_gift.availability_total,
            first_sale_date=utils.timestamp_to_datetime(star_gift.first_sale_date),
            last_sale_date=utils.timestamp_to_datetime(star_gift.last_sale_date),
            upgrade_stars=star_gift.upgrade_stars,
            title=star_gift.title
        )


class StarGiftUnique(Object):
    """A unique/collectible star gift.

    Parameters:
        id (``int``):
            Unique identifier of the collectible gift.

        gift_id (``int``):
            Unique ID of the base gift type.

        title (``str``):
            Collectible title.

        slug (``str``):
            Slug for creating deep links.

        num (``int``):
            Unique number among all collectibles of the same type.

        availability_issued (``int``):
            Number of gifts of this type upgraded to collectible.

        availability_total (``int``):
            Total number that can be upgraded.

        require_premium (``bool``, *optional*):
            Whether only Premium users can buy this.

        burned (``bool``, *optional*):
            Whether this gift has been burned.

        crafted (``bool``, *optional*):
            Whether this gift was crafted.

        owner_id (``int``, *optional*):
            User ID of the owner.

        owner_name (``str``, *optional*):
            Name of the owner if ID is not available.

        owner_address (``str``, *optional*):
            TON blockchain address of the owner.

        gift_address (``str``, *optional*):
            TON blockchain address of the NFT.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        gift_id: int,
        title: str,
        slug: str,
        num: int,
        availability_issued: int,
        availability_total: int,
        require_premium: bool = None,
        burned: bool = None,
        crafted: bool = None,
        owner_id: int = None,
        owner_name: str = None,
        owner_address: str = None,
        gift_address: str = None
    ):
        super().__init__(client)

        self.id = id
        self.gift_id = gift_id
        self.title = title
        self.slug = slug
        self.num = num
        self.availability_issued = availability_issued
        self.availability_total = availability_total
        self.require_premium = require_premium
        self.burned = burned
        self.crafted = crafted
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_address = owner_address
        self.gift_address = gift_address

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        star_gift: "raw.types.StarGiftUnique"
    ) -> "StarGiftUnique":
        owner_id = None
        if star_gift.owner_id:
            owner_id = utils.get_raw_peer_id(star_gift.owner_id)

        return StarGiftUnique(
            client=client,
            id=star_gift.id,
            gift_id=star_gift.gift_id,
            title=star_gift.title,
            slug=star_gift.slug,
            num=star_gift.num,
            availability_issued=star_gift.availability_issued,
            availability_total=star_gift.availability_total,
            require_premium=star_gift.require_premium or None,
            burned=star_gift.burned or None,
            crafted=star_gift.crafted or None,
            owner_id=owner_id,
            owner_name=star_gift.owner_name,
            owner_address=star_gift.owner_address,
            gift_address=star_gift.gift_address
        )
