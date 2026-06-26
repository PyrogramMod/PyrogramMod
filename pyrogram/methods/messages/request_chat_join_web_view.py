from typing import Optional

import pyrogram
from pyrogram import raw


class RequestChatJoinWebView:
    async def request_chat_join_web_view(
        self: "pyrogram.Client",
        query_id: int,
        platform: str,
        theme_params: Optional[dict] = None
    ) -> "raw.base.WebViewResultUrl":
        """Request a web view URL for a chat join button.

        Used when a bot sends a web view button as part of a
        ``chatInviteJoinResultWebView`` response.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            query_id (``int``):
                The query ID from the invite join result.

            platform (``str``):
                Client platform string (e.g. ``"android"``, ``"ios"``, ``"web"``).

            theme_params (``dict``, *optional*):
                Theme parameters as a JSON-serializable dict.

        Returns:
            :obj:`~pyrogram.raw.base.WebViewResultUrl`: The web view URL.

        Example:
            .. code-block:: python

                result = await app.request_chat_join_web_view(
                    query_id=123456,
                    platform="android"
                )
                print(result.url)
        """

        import json

        theme = None
        if theme_params is not None:
            theme = raw.types.DataJSON(data=json.dumps(theme_params))

        return await self.invoke(
            raw.functions.messages.RequestChatJoinWebView(
                query_id=query_id,
                platform=platform,
                theme_params=theme
            )
        )
