from typing import Union, Optional, List

import pyrogram
from pyrogram import raw
from pyrogram import types


class TranslateRichMessage:
    async def translate_rich_message(
        self: "pyrogram.Client",
        to_lang: str,
        chat_id: Optional[Union[int, str]] = None,
        message_ids: Optional[List[int]] = None,
        tone: Optional[str] = None
    ) -> "types.List":
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
            :obj:`~pyrogram.types.List` of :obj:`~pyrogram.types.RichMessage`: Translated messages.

        Example:
            .. code-block:: python

                result = await app.translate_rich_message("en", chat_id=chat_id, message_ids=[123])
                for msg in result:
                    print(msg)
        """

        peer = await self.resolve_peer(chat_id) if chat_id is not None else None

        r = await self.invoke(
            raw.functions.messages.TranslateRichMessage(
                to_lang=to_lang,
                peer=peer,
                id=message_ids,
                tone=tone
            )
        )

        messages = types.List()

        for rich_msg in r.result:
            messages.append(types.RichMessage._parse(self, rich_msg))

        return messages
