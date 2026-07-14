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

from pyrogram import raw, types
from ..object import Object


class KeyboardButton(Object):
    """One button of the reply keyboard.
    For simple text buttons String can be used instead of this object to specify text of the button.
    Optional fields are mutually exclusive.

    Parameters:
        text (``str``):
            Text of the button. If none of the optional fields are used, it will be sent as a message when
            the button is pressed.

        request_contact (``bool``, *optional*):
            If True, the user's phone number will be sent as a contact when the button is pressed.
            Available in private chats only.

        request_location (``bool``, *optional*):
            If True, the user's current location will be sent when the button is pressed.
            Available in private chats only.

        web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):
            If specified, the described `Web App <https://core.telegram.org/bots/webapps>`_ will be launched when the
            button is pressed. The Web App will be able to send a "web_app_data" service message. Available in private
            chats only.

        style (:obj:`~pyrogram.types.KeyboardButtonStyle`, *optional*):
            Style configuration for the button (background color, icon).

    """

    def __init__(
        self,
        text: str,
        request_contact: bool = None,
        request_location: bool = None,
        web_app: "types.WebAppInfo" = None,
        style: "types.KeyboardButtonStyle" = None
    ):
        super().__init__()

        self.text = str(text)
        self.request_contact = request_contact
        self.request_location = request_location
        self.web_app = web_app
        self.style = style

    @staticmethod
    def read(b):
        style = types.KeyboardButtonStyle.read(getattr(b, "style", None))

        if isinstance(b, raw.types.KeyboardButton):
            if style:
                return KeyboardButton(text=b.text, style=style)
            return b.text

        if isinstance(b, raw.types.KeyboardButtonRequestPhone):
            return KeyboardButton(
                text=b.text,
                request_contact=True,
                style=style
            )

        if isinstance(b, raw.types.KeyboardButtonRequestGeoLocation):
            return KeyboardButton(
                text=b.text,
                request_location=True,
                style=style
            )

        if isinstance(b, raw.types.KeyboardButtonSimpleWebView):
            return KeyboardButton(
                text=b.text,
                web_app=types.WebAppInfo(
                    url=b.url
                ),
                style=style
            )

    def write(self):
        style = self.style.write() if self.style else None

        if self.request_contact:
            return raw.types.KeyboardButtonRequestPhone(text=self.text, style=style)
        elif self.request_location:
            return raw.types.KeyboardButtonRequestGeoLocation(text=self.text, style=style)
        elif self.web_app:
            return raw.types.KeyboardButtonSimpleWebView(text=self.text, url=self.web_app.url, style=style)
        else:
            return raw.types.KeyboardButton(text=self.text, style=style)
