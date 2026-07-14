from typing import Optional

import pyrogram
from pyrogram import raw


class ComposeRichMessageWithAI:
    async def compose_rich_message_with_ai(
        self: "pyrogram.Client",
        proofread: bool = False,
        text: Optional["raw.base.InputRichMessage"] = None,
        translate_to_lang: Optional[str] = None,
        tone: Optional["raw.base.InputAiComposeTone"] = None
    ) -> "raw.base.ComposedRichMessageWithAI":
        """Compose or improve a rich message using Telegram's AI.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            proofread (``bool``, *optional*):
                Pass True to proofread and improve the existing ``text``. Defaults to False.

            text (:obj:`~pyrogram.raw.base.InputRichMessage`, *optional*):
                The rich message input to compose or proofread.

            translate_to_lang (``str``, *optional*):
                Target language code for AI-assisted translation.

            tone (:obj:`~pyrogram.raw.base.InputAiComposeTone`, *optional*):
                The composition tone/style to apply.

        Returns:
            :obj:`~pyrogram.raw.base.ComposedRichMessageWithAI`: The AI-composed message.

        Example:
            .. code-block:: python

                result = await app.compose_rich_message_with_ai(
                    proofread=True,
                    text=raw.types.InputRichMessage(blocks=[...])
                )
        """

        return await self.invoke(
            raw.functions.messages.ComposeRichMessageWithAI(
                proofread=proofread or None,
                text=text,
                translate_to_lang=translate_to_lang,
                tone=tone
            )
        )
