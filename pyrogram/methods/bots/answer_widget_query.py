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

from typing import Union

import pyrogram
from pyrogram import raw


class AnswerWidgetQuery:
    async def answer_widget_query(
        self: "pyrogram.Client",
        widget_query_id: Union[int, str],
        data: str = ""
    ) -> bool:
        """Answer a query sent by a widget (Bot API 10.4 ``answerWidgetQuery``).

        Every :obj:`~pyrogram.types.WidgetQuery` must be answered, also when something failed:
        an unanswered query ends in the widget as ``TIMEOUT`` after 15 seconds.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            widget_query_id (``int`` | ``str``):
                Unique identifier of the query (:attr:`~pyrogram.types.WidgetQuery.id`).

            data (``str``, *optional*):
                Answer sent to the widget, at most 1024 bytes.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.answer_widget_query(query.id, '{"ok":true}')
        """
        return await self.invoke(
            raw.functions.messages.SetBotWidgetQueryAnswer(
                query_id=int(widget_query_id),
                result=data
            )
        )
