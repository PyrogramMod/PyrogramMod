from typing import Union

import pyrogram
from pyrogram import raw


class GetWelcomeMessages:
    async def get_welcome_messages(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> "raw.base.WelcomeMessages":
        """Get the welcome messages configured for a chat.

        Welcome messages are ephemeral messages a bot sends automatically the first time a user
        interacts with it in a given chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context to get welcome messages for.

        Returns:
            :obj:`~pyrogram.raw.base.WelcomeMessages`: The raw welcome messages list.

        Example:
            .. code-block:: python

                messages = await app.get_welcome_messages(chat_id)
        """
        return await self.invoke(
            raw.functions.ephemeral.GetWelcomeMessages(
                peer=await self.resolve_peer(chat_id),
                hash=0
            )
        )
