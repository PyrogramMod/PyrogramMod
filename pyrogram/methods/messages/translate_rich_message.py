from typing import Union, Optional, List

import pyrogram
from pyrogram import raw


class TranslateRichMessage:
    async def translate_rich_message(
        self: "pyrogram.Client",
        to_lang: str,
        chat_id: Optional[Union[int, str]] = None,
        message_ids: Optional[List[int]] = None,
        tone: Optional[str] = None
    ) -> "raw.base.messages.TranslatedRichMessage":
        """Translate a rich message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            to_lang (``str``):
                Target language code (e.g. ``"en"``, ``"it"``).

            chat_id (``int`` | ``str``, *optional*):
                Chat containing the rich messages to translate.

            message_ids (List of ``int``, *optional*):
                IDs of the rich messages to translate.

            tone (``str``, *optional*):
                Optional tone/style for the translation.

        Returns:
            :obj:`~pyrogram.raw.base.messages.TranslatedRichMessage`: Translated content.

        Example:
            .. code-block:: python

                result = await app.translate_rich_message("en", chat_id=chat_id, message_ids=[123])
        """

        peer = await self.resolve_peer(chat_id) if chat_id is not None else None

        return await self.invoke(
            raw.functions.messages.TranslateRichMessage(
                to_lang=to_lang,
                peer=peer,
                id=message_ids,
                tone=tone
            )
        )
