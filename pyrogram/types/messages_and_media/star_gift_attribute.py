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
from pyrogram import raw, types
from ..object import Object


class StarGiftAttributeRarity(Object):
    """Rarity information for a star gift attribute.

    Parameters:
        type (``str``):
            Rarity type. One of: "uncommon", "rare", "epic", "legendary".

        permille (``int``):
            Rarity permille (0-1000, where 1000 = 100%).
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        type: str,
        permille: int
    ):
        super().__init__(client)

        self.type = type
        self.permille = permille

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        rarity: "raw.base.StarGiftAttributeRarity"
    ) -> Optional["StarGiftAttributeRarity"]:
        if rarity is None:
            return None

        rarity_type = "unknown"
        if isinstance(rarity, raw.types.StarGiftAttributeRarityUncommon):
            rarity_type = "uncommon"
        elif isinstance(rarity, raw.types.StarGiftAttributeRarityRare):
            rarity_type = "rare"
        elif isinstance(rarity, raw.types.StarGiftAttributeRarityEpic):
            rarity_type = "epic"
        elif isinstance(rarity, raw.types.StarGiftAttributeRarityLegendary):
            rarity_type = "legendary"

        return StarGiftAttributeRarity(
            client=client,
            type=rarity_type,
            permille=rarity.permille
        )


class StarGiftAttribute(Object):
    """Represents an attribute of a collectible star gift.

    Parameters:
        type (``str``):
            Type of the attribute. One of:
            - "backdrop": The backdrop/background of the gift
            - "model": The 3D model of the gift
            - "pattern": The pattern applied to the gift
            - "original_details": Original sender/receiver details

        name (``str``, *optional*):
            Name of the attribute (for backdrop, model, pattern).

        rarity (:obj:`~pyrogram.types.StarGiftAttributeRarity`, *optional*):
            Rarity information for this attribute.

        backdrop_id (``int``, *optional*):
            For "backdrop" type: unique ID of the backdrop.

        center_color (``int``, *optional*):
            For "backdrop" type: center color in RGB24.

        edge_color (``int``, *optional*):
            For "backdrop" type: edge color in RGB24.

        pattern_color (``int``, *optional*):
            For "backdrop" type: pattern color in RGB24.

        text_color (``int``, *optional*):
            For "backdrop" type: text color in RGB24.

        sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
            For "model" type: the sticker representing the model.

        model_id (``int``, *optional*):
            For "model" type: unique ID of the model.

        pattern_id (``int``, *optional*):
            For "pattern" type: unique ID of the pattern.

        document (:obj:`~pyrogram.types.Document`, *optional*):
            For "pattern" type: the pattern document.

        sender_id (``int``, *optional*):
            For "original_details" type: original sender user ID.

        recipient_id (``int``, *optional*):
            For "original_details" type: original recipient user ID.

        date (:py:obj:`~datetime.datetime`, *optional*):
            For "original_details" type: when the gift was sent.

        message (``str``, *optional*):
            For "original_details" type: original gift message.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        type: str,
        name: str = None,
        rarity: "StarGiftAttributeRarity" = None,
        backdrop_id: int = None,
        center_color: int = None,
        edge_color: int = None,
        pattern_color: int = None,
        text_color: int = None,
        sticker: "types.Sticker" = None,
        model_id: int = None,
        pattern_id: int = None,
        document: "types.Document" = None,
        sender_id: int = None,
        recipient_id: int = None,
        date: "datetime" = None,
        message: str = None
    ):
        super().__init__(client)

        self.type = type
        self.name = name
        self.rarity = rarity
        self.backdrop_id = backdrop_id
        self.center_color = center_color
        self.edge_color = edge_color
        self.pattern_color = pattern_color
        self.text_color = text_color
        self.sticker = sticker
        self.model_id = model_id
        self.pattern_id = pattern_id
        self.document = document
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.date = date
        self.message = message

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        attribute: "raw.base.StarGiftAttribute"
    ) -> Optional["StarGiftAttribute"]:
        from datetime import datetime
        from pyrogram import utils

        if isinstance(attribute, raw.types.StarGiftAttributeBackdrop):
            return StarGiftAttribute(
                client=client,
                type="backdrop",
                name=attribute.name,
                rarity=StarGiftAttributeRarity._parse(client, attribute.rarity),
                backdrop_id=attribute.backdrop_id,
                center_color=attribute.center_color,
                edge_color=attribute.edge_color,
                pattern_color=attribute.pattern_color,
                text_color=attribute.text_color
            )
        elif isinstance(attribute, raw.types.StarGiftAttributeModel):
            sticker = None
            if attribute.document:
                sticker = await types.Sticker._parse(client, attribute.document, {})

            return StarGiftAttribute(
                client=client,
                type="model",
                name=attribute.name,
                rarity=StarGiftAttributeRarity._parse(client, attribute.rarity),
                sticker=sticker,
                model_id=attribute.model_id
            )
        elif isinstance(attribute, raw.types.StarGiftAttributePattern):
            document = None
            if attribute.document:
                document = types.Document._parse(client, attribute.document, None)

            return StarGiftAttribute(
                client=client,
                type="pattern",
                name=attribute.name,
                rarity=StarGiftAttributeRarity._parse(client, attribute.rarity),
                pattern_id=attribute.pattern_id,
                document=document
            )
        elif isinstance(attribute, raw.types.StarGiftAttributeOriginalDetails):
            sender_id = None
            recipient_id = None

            if attribute.sender_id:
                sender_id = utils.get_raw_peer_id(attribute.sender_id)
            if attribute.recipient_id:
                recipient_id = utils.get_raw_peer_id(attribute.recipient_id)

            return StarGiftAttribute(
                client=client,
                type="original_details",
                sender_id=sender_id,
                recipient_id=recipient_id,
                date=utils.timestamp_to_datetime(attribute.date),
                message=attribute.message
            )

        return None

    @staticmethod
    async def _parse_list(
        client: "pyrogram.Client",
        attributes: List["raw.base.StarGiftAttribute"]
    ) -> Optional[List["StarGiftAttribute"]]:
        if not attributes:
            return None

        result = []
        for attr in attributes:
            parsed = await StarGiftAttribute._parse(client, attr)
            if parsed:
                result.append(parsed)

        return types.List(result) if result else None
