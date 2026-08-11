from typing import Union, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetEphemeralCallbackAnswer:
    async def get_ephemeral_callback_answer(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        data: Optional[bytes] = None
    ) -> "types.CallbackAnswer":
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
            :obj:`~pyrogram.types.CallbackAnswer`: The bot callback answer.

        Example:
            .. code-block:: python

                answer = await app.get_ephemeral_callback_answer(chat_id, 123, b"action")
                print(answer.message)
        """

        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.ephemeral.GetCallbackAnswer(
                peer=peer,
                id=message_id,
                data=data
            )
        )

        return types.CallbackAnswer._parse(self, r)
