from typing import Union, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class ForwardWelcomeMessage:
    async def forward_welcome_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
    ) -> Optional["types.Message"]:
        """Forward a welcome message into its chat, sending it as a regular message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context the welcome message belongs to.

            message_id (``int``):
                Identifier of the welcome message to forward.

        Returns:
            :obj:`~pyrogram.types.Message` | ``None``: On success, the forwarded message is returned,
            otherwise None.

        Example:
            .. code-block:: python

                await app.forward_welcome_message(chat_id, 123)
        """
        r = await self.invoke(
            raw.functions.messages.ForwardMessage(
                peer=await self.resolve_peer(chat_id),
                id=message_id,
                random_id=self.rnd_id()
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                              raw.types.UpdateNewChannelMessage)):
                return await types.Message._parse(
                    self, i.message, users, chats
                )

        return None
