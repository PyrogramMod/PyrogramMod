from typing import Union, Optional

import pyrogram
from pyrogram import raw


class GetEphemeralCallbackAnswer:
    async def get_ephemeral_callback_answer(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        data: Optional[bytes] = None
    ) -> "raw.base.messages.BotCallbackAnswer":
        """Get a callback answer for an ephemeral message inline button.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context of the ephemeral message.

            message_id (``int``):
                The ephemeral message ID.

            data (``bytes``, *optional*):
                Callback data.

        Returns:
            :obj:`~pyrogram.raw.base.messages.BotCallbackAnswer`: The bot callback answer.

        Example:
            .. code-block:: python

                answer = await app.get_ephemeral_callback_answer(chat_id, 123, b"action")
        """

        peer = await self.resolve_peer(chat_id)

        return await self.invoke(
            raw.functions.ephemeral.GetCallbackAnswer(
                peer=peer,
                id=message_id,
                data=data
            )
        )
