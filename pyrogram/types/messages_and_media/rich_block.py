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


class RichBlockTableCell(Object):
    """A single cell inside a :obj:`~pyrogram.types.RichBlock` TABLE.

    Parameters:
        text (:obj:`~pyrogram.types.RichText`, *optional*):
            Cell content.

        colspan (``int``, *optional*):
            Column span.

        rowspan (``int``, *optional*):
            Row span.

        header (``bool``, *optional*):
            True if this is a header cell.

        align_center (``bool``, *optional*):
            Horizontally centered.

        align_right (``bool``, *optional*):
            Right-aligned.

        valign_middle (``bool``, *optional*):
            Vertically centered.

        valign_bottom (``bool``, *optional*):
            Bottom-aligned.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        text: Optional["pyrogram.types.RichText"] = None,
        colspan: Optional[int] = None,
        rowspan: Optional[int] = None,
        header: bool = False,
        align_center: bool = False,
        align_right: bool = False,
        valign_middle: bool = False,
        valign_bottom: bool = False,
    ):
        super().__init__(client)
        self.text = text
        self.colspan = colspan
        self.rowspan = rowspan
        self.header = header
        self.align_center = align_center
        self.align_right = align_right
        self.valign_middle = valign_middle
        self.valign_bottom = valign_bottom

    @staticmethod
    def _parse(client: "pyrogram.Client", raw_cell: "raw.types.PageTableCell") -> "RichBlockTableCell":
        from .rich_text import RichText
        return RichBlockTableCell(
            client=client,
            text=RichText._parse(client, raw_cell.text) if raw_cell.text else None,
            colspan=raw_cell.colspan,
            rowspan=raw_cell.rowspan,
            header=raw_cell.header or False,
            align_center=raw_cell.align_center or False,
            align_right=raw_cell.align_right or False,
            valign_middle=raw_cell.valign_middle or False,
            valign_bottom=raw_cell.valign_bottom or False,
        )


class RichBlock(Object):
    """A block element inside a :obj:`~pyrogram.types.RichMessage`.

    Parameters:
        type (:obj:`~pyrogram.enums.RichBlockType`):
            Block type.

        text (:obj:`~pyrogram.types.RichText`, *optional*):
            Primary text content.

        caption_text (:obj:`~pyrogram.types.RichText`, *optional*):
            Caption text (for media blocks).

        caption_credit (:obj:`~pyrogram.types.RichText`, *optional*):
            Caption credit line.

        blocks (List of :obj:`~pyrogram.types.RichBlock`, *optional*):
            Nested blocks.

        items (List of :obj:`~pyrogram.types.RichBlock`, *optional*):
            List items (each item is a block).

        rows (List of List of :obj:`~pyrogram.types.RichBlockTableCell`, *optional*):
            Table rows (TABLE type).

        author (``str``, *optional*):
            Author name (AUTHOR_DATE, EMBED_POST types).

        published_date (:py:obj:`~datetime.datetime`, *optional*):
            Publication date (AUTHOR_DATE type).

        language (``str``, *optional*):
            Programming language (PREFORMATTED type).

        photo_id (``int``, *optional*):
            Photo document ID (PHOTO type).

        video_id (``int``, *optional*):
            Video document ID (VIDEO type).

        audio_id (``int``, *optional*):
            Audio document ID (AUDIO type).

        url (``str``, *optional*):
            URL (EMBED, EMBED_POST, PHOTO types).

        html (``str``, *optional*):
            Raw HTML (EMBED type).

        anchor_name (``str``, *optional*):
            Anchor name (ANCHOR type).

        math_source (``str``, *optional*):
            LaTeX source (MATH type).

        open (``bool``, *optional*):
            Whether the DETAILS block is expanded by default.

        autoplay (``bool``, *optional*):
            Auto-play flag (VIDEO type).

        loop (``bool``, *optional*):
            Loop flag (VIDEO type).

        full_width (``bool``, *optional*):
            Full-width flag (EMBED type).

        allow_scrolling (``bool``, *optional*):
            Scrolling flag (EMBED type).

        bordered (``bool``, *optional*):
            Bordered table (TABLE type).

        striped (``bool``, *optional*):
            Striped table (TABLE type).

        ordered_start (``int``, *optional*):
            Starting number for ORDERED_LIST.

        ordered_reversed (``bool``, *optional*):
            Reversed order for ORDERED_LIST.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        type: "enums.RichBlockType",
        text: Optional["pyrogram.types.RichText"] = None,
        caption_text: Optional["pyrogram.types.RichText"] = None,
        caption_credit: Optional["pyrogram.types.RichText"] = None,
        blocks: Optional[List["RichBlock"]] = None,
        items: Optional[List["RichBlock"]] = None,
        rows: Optional[List[List["RichBlockTableCell"]]] = None,
        author: Optional[str] = None,
        published_date: Optional[datetime] = None,
        language: Optional[str] = None,
        photo_id: Optional[int] = None,
        video_id: Optional[int] = None,
        audio_id: Optional[int] = None,
        url: Optional[str] = None,
        html: Optional[str] = None,
        anchor_name: Optional[str] = None,
        math_source: Optional[str] = None,
        open: Optional[bool] = None,
        autoplay: Optional[bool] = None,
        loop: Optional[bool] = None,
        full_width: Optional[bool] = None,
        allow_scrolling: Optional[bool] = None,
        bordered: Optional[bool] = None,
        striped: Optional[bool] = None,
        ordered_start: Optional[int] = None,
        ordered_reversed: Optional[bool] = None,
    ):
        super().__init__(client)
        self.type = type
        self.text = text
        self.caption_text = caption_text
        self.caption_credit = caption_credit
        self.blocks = blocks
        self.items = items
        self.rows = rows
        self.author = author
        self.published_date = published_date
        self.language = language
        self.photo_id = photo_id
        self.video_id = video_id
        self.audio_id = audio_id
        self.url = url
        self.html = html
        self.anchor_name = anchor_name
        self.math_source = math_source
        self.open = open
        self.autoplay = autoplay
        self.loop = loop
        self.full_width = full_width
        self.allow_scrolling = allow_scrolling
        self.bordered = bordered
        self.striped = striped
        self.ordered_start = ordered_start
        self.ordered_reversed = ordered_reversed

    @staticmethod
    def _parse(client: "pyrogram.Client", raw_block: "raw.base.PageBlock") -> Optional["RichBlock"]:
        from .rich_text import RichText

        def _rt(t):
            return RichText._parse(client, t)

        def _caption(cap):
            if cap is None:
                return None, None
            return _rt(cap.text), _rt(cap.credit)

        def _rb(b):
            return RichBlock._parse(client, b)

        if isinstance(raw_block, raw.types.PageBlockUnsupported):
            return RichBlock(client=client, type=enums.RichBlockType.UNSUPPORTED)

        if isinstance(raw_block, raw.types.PageBlockTitle):
            return RichBlock(client=client, type=enums.RichBlockType.TITLE, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockSubtitle):
            return RichBlock(client=client, type=enums.RichBlockType.SUBTITLE, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockAuthorDate):
            return RichBlock(
                client=client,
                type=enums.RichBlockType.AUTHOR_DATE,
                author=_rt(raw_block.author).plain_text if _rt(raw_block.author) else None,
                text=_rt(raw_block.author),
                published_date=utils.timestamp_to_datetime(raw_block.published_date) if raw_block.published_date else None,
            )

        if isinstance(raw_block, raw.types.PageBlockHeader):
            return RichBlock(client=client, type=enums.RichBlockType.HEADER, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockSubheader):
            return RichBlock(client=client, type=enums.RichBlockType.SUBHEADER, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockParagraph):
            return RichBlock(client=client, type=enums.RichBlockType.PARAGRAPH, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockPreformatted):
            return RichBlock(
                client=client,
                type=enums.RichBlockType.PREFORMATTED,
                text=_rt(raw_block.text),
                language=raw_block.language,
            )

        if isinstance(raw_block, raw.types.PageBlockFooter):
            return RichBlock(client=client, type=enums.RichBlockType.FOOTER, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockDivider):
            return RichBlock(client=client, type=enums.RichBlockType.DIVIDER)

        if isinstance(raw_block, raw.types.PageBlockAnchor):
            return RichBlock(client=client, type=enums.RichBlockType.ANCHOR, anchor_name=raw_block.name)

        if isinstance(raw_block, raw.types.PageBlockKicker):
            return RichBlock(client=client, type=enums.RichBlockType.KICKER, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockBlockquote):
            ct, cc = _caption(None)
            return RichBlock(
                client=client,
                type=enums.RichBlockType.BLOCKQUOTE,
                text=_rt(raw_block.text),
                caption_text=_rt(raw_block.caption),
            )

        if isinstance(raw_block, raw.types.PageBlockBlockquoteBlocks):
            return RichBlock(
                client=client,
                type=enums.RichBlockType.BLOCKQUOTE_BLOCKS,
                blocks=[_rb(b) for b in raw_block.blocks],
                caption_text=_rt(raw_block.caption),
            )

        if isinstance(raw_block, raw.types.PageBlockPullquote):
            return RichBlock(
                client=client,
                type=enums.RichBlockType.PULLQUOTE,
                text=_rt(raw_block.text),
                caption_text=_rt(raw_block.caption),
            )

        if isinstance(raw_block, raw.types.PageBlockList):
            list_items = []
            for item in raw_block.items:
                if isinstance(item, raw.types.PageListItemText):
                    list_items.append(RichBlock(client=client, type=enums.RichBlockType.PARAGRAPH, text=_rt(item.text)))
                elif isinstance(item, raw.types.PageListItemBlocks):
                    list_items.append(RichBlock(client=client, type=enums.RichBlockType.PARAGRAPH, blocks=[_rb(b) for b in item.blocks]))
            return RichBlock(client=client, type=enums.RichBlockType.LIST, items=list_items)

        if isinstance(raw_block, raw.types.PageBlockOrderedList):
            ordered_items = []
            for item in raw_block.items:
                if isinstance(item, raw.types.PageListOrderedItemText):
                    ordered_items.append(RichBlock(client=client, type=enums.RichBlockType.PARAGRAPH, text=_rt(item.text)))
                elif isinstance(item, raw.types.PageListOrderedItemBlocks):
                    ordered_items.append(RichBlock(client=client, type=enums.RichBlockType.PARAGRAPH, blocks=[_rb(b) for b in item.blocks]))
            return RichBlock(
                client=client,
                type=enums.RichBlockType.ORDERED_LIST,
                items=ordered_items,
                ordered_start=getattr(raw_block, "start", None),
                ordered_reversed=getattr(raw_block, "reversed", None),
            )

        if isinstance(raw_block, raw.types.PageBlockPhoto):
            ct, cc = _caption(raw_block.caption)
            return RichBlock(
                client=client,
                type=enums.RichBlockType.PHOTO,
                photo_id=raw_block.photo_id,
                url=raw_block.url,
                caption_text=ct,
                caption_credit=cc,
            )

        if isinstance(raw_block, raw.types.PageBlockVideo):
            ct, cc = _caption(raw_block.caption)
            return RichBlock(
                client=client,
                type=enums.RichBlockType.VIDEO,
                video_id=raw_block.video_id,
                autoplay=raw_block.autoplay,
                loop=raw_block.loop,
                caption_text=ct,
                caption_credit=cc,
            )

        if isinstance(raw_block, raw.types.PageBlockCover):
            return RichBlock(client=client, type=enums.RichBlockType.COVER, blocks=[_rb(raw_block.cover)])

        if isinstance(raw_block, raw.types.PageBlockEmbed):
            ct, cc = _caption(raw_block.caption)
            return RichBlock(
                client=client,
                type=enums.RichBlockType.EMBED,
                url=raw_block.url,
                html=raw_block.html,
                full_width=raw_block.full_width,
                allow_scrolling=raw_block.allow_scrolling,
                caption_text=ct,
                caption_credit=cc,
            )

        if isinstance(raw_block, raw.types.PageBlockEmbedPost):
            ct, cc = _caption(raw_block.caption)
            return RichBlock(
                client=client,
                type=enums.RichBlockType.EMBED_POST,
                url=raw_block.url,
                author=raw_block.author,
                published_date=utils.timestamp_to_datetime(raw_block.date) if raw_block.date else None,
                blocks=[_rb(b) for b in raw_block.blocks],
                caption_text=ct,
                caption_credit=cc,
            )

        if isinstance(raw_block, raw.types.PageBlockCollage):
            ct, cc = _caption(raw_block.caption)
            return RichBlock(
                client=client,
                type=enums.RichBlockType.COLLAGE,
                items=[_rb(b) for b in raw_block.items],
                caption_text=ct,
                caption_credit=cc,
            )

        if isinstance(raw_block, raw.types.PageBlockSlideshow):
            ct, cc = _caption(raw_block.caption)
            return RichBlock(
                client=client,
                type=enums.RichBlockType.SLIDESHOW,
                items=[_rb(b) for b in raw_block.items],
                caption_text=ct,
                caption_credit=cc,
            )

        if isinstance(raw_block, raw.types.PageBlockAudio):
            ct, cc = _caption(raw_block.caption)
            return RichBlock(
                client=client,
                type=enums.RichBlockType.AUDIO,
                audio_id=raw_block.audio_id,
                caption_text=ct,
                caption_credit=cc,
            )

        if isinstance(raw_block, raw.types.PageBlockTable):
            row_list = []
            for row in raw_block.rows:
                row_list.append([RichBlockTableCell._parse(client, cell) for cell in row.cells])
            return RichBlock(
                client=client,
                type=enums.RichBlockType.TABLE,
                text=_rt(raw_block.title),
                rows=row_list,
                bordered=raw_block.bordered,
                striped=raw_block.striped,
            )

        if isinstance(raw_block, raw.types.PageBlockDetails):
            return RichBlock(
                client=client,
                type=enums.RichBlockType.DETAILS,
                text=_rt(raw_block.title),
                blocks=[_rb(b) for b in raw_block.blocks],
                open=raw_block.open,
            )

        if isinstance(raw_block, raw.types.PageBlockMap):
            ct, cc = _caption(raw_block.caption)
            return RichBlock(
                client=client,
                type=enums.RichBlockType.MAP,
                caption_text=ct,
                caption_credit=cc,
            )

        if isinstance(raw_block, raw.types.PageBlockMath):
            return RichBlock(client=client, type=enums.RichBlockType.MATH, math_source=raw_block.source)

        if isinstance(raw_block, raw.types.PageBlockThinking):
            return RichBlock(client=client, type=enums.RichBlockType.THINKING, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockHeading1):
            return RichBlock(client=client, type=enums.RichBlockType.HEADING1, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockHeading2):
            return RichBlock(client=client, type=enums.RichBlockType.HEADING2, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockHeading3):
            return RichBlock(client=client, type=enums.RichBlockType.HEADING3, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockHeading4):
            return RichBlock(client=client, type=enums.RichBlockType.HEADING4, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockHeading5):
            return RichBlock(client=client, type=enums.RichBlockType.HEADING5, text=_rt(raw_block.text))

        if isinstance(raw_block, raw.types.PageBlockHeading6):
            return RichBlock(client=client, type=enums.RichBlockType.HEADING6, text=_rt(raw_block.text))

        return RichBlock(client=client, type=enums.RichBlockType.UNSUPPORTED)
