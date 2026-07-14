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

from enum import auto

from .auto_name import AutoName


class RichBlockType(AutoName):
    """Rich block element type enumeration used in :obj:`~pyrogram.types.RichBlock`."""

    UNSUPPORTED = auto()
    "Unsupported block"

    TITLE = auto()
    "Document title"

    SUBTITLE = auto()
    "Document subtitle"

    AUTHOR_DATE = auto()
    "Author and publication date"

    HEADER = auto()
    "Section header"

    SUBHEADER = auto()
    "Section subheader"

    PARAGRAPH = auto()
    "Text paragraph"

    PREFORMATTED = auto()
    "Preformatted / code block"

    FOOTER = auto()
    "Document footer"

    DIVIDER = auto()
    "Horizontal divider"

    ANCHOR = auto()
    "Named anchor"

    LIST = auto()
    "Unordered list"

    ORDERED_LIST = auto()
    "Ordered (numbered) list"

    BLOCKQUOTE = auto()
    "Block quotation (text + caption as RichText)"

    BLOCKQUOTE_BLOCKS = auto()
    "Block quotation with nested blocks"

    PULLQUOTE = auto()
    "Pull quotation"

    PHOTO = auto()
    "Photo block"

    VIDEO = auto()
    "Video block"

    COVER = auto()
    "Cover block"

    EMBED = auto()
    "Embedded content"

    EMBED_POST = auto()
    "Embedded post"

    COLLAGE = auto()
    "Photo collage"

    SLIDESHOW = auto()
    "Slideshow"

    CHANNEL = auto()
    "Channel reference"

    AUDIO = auto()
    "Audio block"

    KICKER = auto()
    "Kicker / eyebrow text"

    TABLE = auto()
    "Table"

    DETAILS = auto()
    "Collapsible details block"

    RELATED_ARTICLES = auto()
    "Related articles"

    MAP = auto()
    "Map block"

    HEADING1 = auto()
    "Heading level 1"

    HEADING2 = auto()
    "Heading level 2"

    HEADING3 = auto()
    "Heading level 3"

    HEADING4 = auto()
    "Heading level 4"

    HEADING5 = auto()
    "Heading level 5"

    HEADING6 = auto()
    "Heading level 6"

    MATH = auto()
    "Mathematical expression block"

    THINKING = auto()
    "AI thinking / reasoning block"
