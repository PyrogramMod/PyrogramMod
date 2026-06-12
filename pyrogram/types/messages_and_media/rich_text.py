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
from typing import List, Optional

import pyrogram
from pyrogram import raw, enums, utils
from ..object import Object


class RichText(Object):
    """A rich formatted text element.

    Parameters:
        type (:obj:`~pyrogram.enums.RichTextType`):
            Type of the rich text element.

        plain_text (``str``, *optional*):
            Plain text content (for PLAIN type).

        text (:obj:`~pyrogram.types.RichText`, *optional*):
            Nested rich text (for single-child types like BOLD, ITALIC, etc.).

        texts (List of :obj:`~pyrogram.types.RichText`, *optional*):
            Multiple child elements (for CONCAT type).

        url (``str``, *optional*):
            URL (for URL type).

        webpage_id (``int``, *optional*):
            Webpage ID (for URL type).

        email (``str``, *optional*):
            Email address (for EMAIL type).

        phone (``str``, *optional*):
            Phone number (for PHONE type).

        bank_card (``str``, *optional*):
            Bank card number (for BANK_CARD type).

        document_id (``int``, *optional*):
            Document ID (for IMAGE type).

        image_width (``int``, *optional*):
            Image display width (for IMAGE type).

        image_height (``int``, *optional*):
            Image display height (for IMAGE type).

        anchor_name (``str``, *optional*):
            Anchor name (for ANCHOR type).

        math_source (``str``, *optional*):
            LaTeX source (for MATH type).

        custom_emoji_id (``int``, *optional*):
            Custom emoji document ID (for CUSTOM_EMOJI type).

        custom_emoji_alt (``str``, *optional*):
            Fallback text for the custom emoji (for CUSTOM_EMOJI type).

        user_id (``int``, *optional*):
            User ID (for MENTION_NAME type).

        date (:py:obj:`~datetime.datetime`, *optional*):
            Date/time value (for DATE type).

        date_relative (``bool``, *optional*):
            Show as relative time (for DATE type).

        date_short_time (``bool``, *optional*):
            Show short time (for DATE type).

        date_long_time (``bool``, *optional*):
            Show long time (for DATE type).

        date_short_date (``bool``, *optional*):
            Show short date (for DATE type).

        date_long_date (``bool``, *optional*):
            Show long date (for DATE type).

        date_day_of_week (``bool``, *optional*):
            Show day of week (for DATE type).
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        type: "enums.RichTextType",
        plain_text: Optional[str] = None,
        text: Optional["RichText"] = None,
        texts: Optional[List["RichText"]] = None,
        url: Optional[str] = None,
        webpage_id: Optional[int] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        bank_card: Optional[str] = None,
        document_id: Optional[int] = None,
        image_width: Optional[int] = None,
        image_height: Optional[int] = None,
        anchor_name: Optional[str] = None,
        math_source: Optional[str] = None,
        custom_emoji_id: Optional[int] = None,
        custom_emoji_alt: Optional[str] = None,
        user_id: Optional[int] = None,
        date: Optional[datetime] = None,
        date_relative: Optional[bool] = None,
        date_short_time: Optional[bool] = None,
        date_long_time: Optional[bool] = None,
        date_short_date: Optional[bool] = None,
        date_long_date: Optional[bool] = None,
        date_day_of_week: Optional[bool] = None,
    ):
        super().__init__(client)

        self.type = type
        self.plain_text = plain_text
        self.text = text
        self.texts = texts
        self.url = url
        self.webpage_id = webpage_id
        self.email = email
        self.phone = phone
        self.bank_card = bank_card
        self.document_id = document_id
        self.image_width = image_width
        self.image_height = image_height
        self.anchor_name = anchor_name
        self.math_source = math_source
        self.custom_emoji_id = custom_emoji_id
        self.custom_emoji_alt = custom_emoji_alt
        self.user_id = user_id
        self.date = date
        self.date_relative = date_relative
        self.date_short_time = date_short_time
        self.date_long_time = date_long_time
        self.date_short_date = date_short_date
        self.date_long_date = date_long_date
        self.date_day_of_week = date_day_of_week

    @staticmethod
    def _parse(client: "pyrogram.Client", raw_text: "raw.base.RichText") -> Optional["RichText"]:
        if raw_text is None:
            return None

        if isinstance(raw_text, raw.types.TextEmpty):
            return RichText(client=client, type=enums.RichTextType.EMPTY)

        if isinstance(raw_text, raw.types.TextPlain):
            return RichText(client=client, type=enums.RichTextType.PLAIN, plain_text=raw_text.text)

        if isinstance(raw_text, raw.types.TextBold):
            return RichText(client=client, type=enums.RichTextType.BOLD, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextItalic):
            return RichText(client=client, type=enums.RichTextType.ITALIC, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextUnderline):
            return RichText(client=client, type=enums.RichTextType.UNDERLINE, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextStrike):
            return RichText(client=client, type=enums.RichTextType.STRIKE, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextFixed):
            return RichText(client=client, type=enums.RichTextType.CODE, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextMarked):
            return RichText(client=client, type=enums.RichTextType.MARKED, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextSubscript):
            return RichText(client=client, type=enums.RichTextType.SUBSCRIPT, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextSuperscript):
            return RichText(client=client, type=enums.RichTextType.SUPERSCRIPT, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextSpoiler):
            return RichText(client=client, type=enums.RichTextType.SPOILER, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextMention):
            return RichText(client=client, type=enums.RichTextType.MENTION, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextHashtag):
            return RichText(client=client, type=enums.RichTextType.HASHTAG, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextBotCommand):
            return RichText(client=client, type=enums.RichTextType.BOT_COMMAND, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextCashtag):
            return RichText(client=client, type=enums.RichTextType.CASHTAG, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextAutoUrl):
            return RichText(client=client, type=enums.RichTextType.AUTO_URL, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextAutoEmail):
            return RichText(client=client, type=enums.RichTextType.AUTO_EMAIL, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextAutoPhone):
            return RichText(client=client, type=enums.RichTextType.AUTO_PHONE, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextBankCard):
            return RichText(client=client, type=enums.RichTextType.BANK_CARD, text=RichText._parse(client, raw_text.text))

        if isinstance(raw_text, raw.types.TextUrl):
            return RichText(
                client=client,
                type=enums.RichTextType.URL,
                text=RichText._parse(client, raw_text.text),
                url=raw_text.url,
                webpage_id=raw_text.webpage_id,
            )

        if isinstance(raw_text, raw.types.TextEmail):
            return RichText(
                client=client,
                type=enums.RichTextType.EMAIL,
                text=RichText._parse(client, raw_text.text),
                email=raw_text.email,
            )

        if isinstance(raw_text, raw.types.TextPhone):
            return RichText(
                client=client,
                type=enums.RichTextType.PHONE,
                text=RichText._parse(client, raw_text.text),
                phone=raw_text.phone,
            )

        if isinstance(raw_text, raw.types.TextConcat):
            return RichText(
                client=client,
                type=enums.RichTextType.CONCAT,
                texts=[RichText._parse(client, t) for t in raw_text.texts],
            )

        if isinstance(raw_text, raw.types.TextImage):
            return RichText(
                client=client,
                type=enums.RichTextType.IMAGE,
                document_id=raw_text.document_id,
                image_width=raw_text.w,
                image_height=raw_text.h,
            )

        if isinstance(raw_text, raw.types.TextAnchor):
            return RichText(
                client=client,
                type=enums.RichTextType.ANCHOR,
                text=RichText._parse(client, raw_text.text),
                anchor_name=raw_text.name,
            )

        if isinstance(raw_text, raw.types.TextMath):
            return RichText(client=client, type=enums.RichTextType.MATH, math_source=raw_text.source)

        if isinstance(raw_text, raw.types.TextCustomEmoji):
            return RichText(
                client=client,
                type=enums.RichTextType.CUSTOM_EMOJI,
                custom_emoji_id=raw_text.document_id,
                custom_emoji_alt=raw_text.alt,
            )

        if isinstance(raw_text, raw.types.TextMentionName):
            return RichText(
                client=client,
                type=enums.RichTextType.MENTION_NAME,
                text=RichText._parse(client, raw_text.text),
                user_id=raw_text.user_id,
            )

        if isinstance(raw_text, raw.types.TextDate):
            return RichText(
                client=client,
                type=enums.RichTextType.DATE,
                text=RichText._parse(client, raw_text.text),
                date=utils.timestamp_to_datetime(raw_text.date),
                date_relative=raw_text.relative,
                date_short_time=raw_text.short_time,
                date_long_time=raw_text.long_time,
                date_short_date=raw_text.short_date,
                date_long_date=raw_text.long_date,
                date_day_of_week=raw_text.day_of_week,
            )

        return RichText(client=client, type=enums.RichTextType.EMPTY)
