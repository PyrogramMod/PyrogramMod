from typing import Union

import pyrogram
from pyrogram import raw


class ForwardWelcomeMessage:
    async def forward_welcome_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
    ) -> "raw.base.Updates":
        """Forward a welcome message into its chat, sending it as a regular message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context the welcome message belongs to.

            message_id (``int``):
                Identifier of the welcome message to forward.

        Returns:
            :obj:`~pyrogram.raw.base.Updates`: On success.

        Example:
            .. code-block:: python

                await app.forward_welcome_message(chat_id, 123)
        """
        return await self.invoke(
            raw.functions.messages.ForwardMessage(
                peer=await self.resolve_peer(chat_id),
                id=message_id,
                random_id=self.rnd_id()
            )
        )
