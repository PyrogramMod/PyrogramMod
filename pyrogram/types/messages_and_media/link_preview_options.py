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

from typing import Optional

import pyrogram
from ..object import Object


class LinkPreviewOptions(Object):
    """Options used to control link preview generation.

    Parameters:
        is_disabled (``bool``, *optional*):
            True if the link preview is disabled.

        show_above_text (``bool``, *optional*):
            True if the media in the link preview is supposed to be shown above the message text.
            Only usable when the link preview is not disabled.

    Example:
        .. code-block:: python

            from pyrogram.types import LinkPreviewOptions

            # Disable preview
            await app.send_message(chat_id, "https://pyrogram.org",
                link_preview_options=LinkPreviewOptions(is_disabled=True))

            # Show preview above the text
            await app.send_message(chat_id, "https://pyrogram.org",
                link_preview_options=LinkPreviewOptions(show_above_text=True))
    """

    def __init__(
        self,
        *,
        is_disabled: Optional[bool] = None,
        show_above_text: Optional[bool] = None
    ):
        super().__init__()

        self.is_disabled = is_disabled
        self.show_above_text = show_above_text
