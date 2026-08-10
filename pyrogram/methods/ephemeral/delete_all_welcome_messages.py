from typing import Union

import pyrogram
from pyrogram import raw


class DeleteAllWelcomeMessages:
    async def delete_all_welcome_messages(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> bool:
        """Delete all welcome messages configured for a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context to clear welcome messages for.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_all_welcome_messages(chat_id)
        """
        return await self.invoke(
            raw.functions.ephemeral.DeleteAllWelcomeMessages(
                peer=await self.resolve_peer(chat_id)
            )
        )
