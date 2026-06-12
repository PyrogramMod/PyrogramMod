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

import pyrogram


class SendChatJoinRequestWebApp:
    async def send_chat_join_request_web_app(
        self: "pyrogram.Client",
        query_id: int,
        url: str,
    ) -> bool:
        """Open a WebApp for the user who sent a join request.

        Shortcut for :meth:`~pyrogram.Client.answer_chat_join_request_query`
        with ``action="web_view"``.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            query_id (``int``):
                Guard-bot query ID from :attr:`~pyrogram.types.ChatJoinRequest.query_id`.

            url (``str``):
                HTTPS URL of the WebApp to open for the joining user.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                @app.on_chat_join_request()
                async def handler(client, request):
                    if request.query_id:
                        await client.send_chat_join_request_web_app(
                            request.query_id,
                            url="https://example.com/captcha"
                        )
        """
        return await self.answer_chat_join_request_query(query_id, "web_view", url=url)
