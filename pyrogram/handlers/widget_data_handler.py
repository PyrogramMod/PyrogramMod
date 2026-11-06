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

from typing import Callable

from .handler import Handler


class WidgetDataHandler(Handler):
    """Handler for widget state changes.
    It is intended to be used with :meth:`~pyrogram.Client.add_handler`, or use the
    :meth:`~pyrogram.Client.on_widget_data` decorator.

    Parameters:
        callback (``Callable``):
            Function called with *(client, update)*, where update is a :obj:`~pyrogram.types.WidgetDataUpdate`.

        filters (:obj:`Filters`):
            Filters to restrict which updates reach the callback.
    """

    def __init__(self, callback: Callable, filters=None):
        super().__init__(callback, filters)
