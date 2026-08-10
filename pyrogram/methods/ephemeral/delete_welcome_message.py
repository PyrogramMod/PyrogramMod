from typing import Union

import pyrogram
from pyrogram import raw


class DeleteWelcomeMessage:
    async def delete_welcome_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
    ) -> bool:
        """Delete a single welcome message from a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context the welcome message belongs to.

            message_id (``int``):
                Identifier of the welcome message to delete.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_welcome_message(chat_id, 123)
        """
        return await self.invoke(
            raw.functions.ephemeral.DeleteWelcomeMessage(
                peer=await self.resolve_peer(chat_id),
                id=message_id
            )
        )
