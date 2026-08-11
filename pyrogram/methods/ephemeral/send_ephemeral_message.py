from typing import Union, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class SendEphemeralMessage:
    async def send_ephemeral_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        receiver_id: Union[int, str],
        text: str,
        query_id: Optional[int] = None
    ) -> Optional["types.Message"]:
        """Send an ephemeral message to a bot within a peer context.

        Ephemeral messages are visible only to the receiver bot and disappear
        once read. Used for private bot interactions within a group context.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context (chat) for the ephemeral message.

            receiver_id (``int`` | ``str``):
                The bot user that will receive the ephemeral message.

            text (``str``):
                The message text.

            query_id (``int``, *optional*):
                Callback query ID, if replying to a bot query.

        Returns:
            :obj:`~pyrogram.types.Message` | ``None``: On success, the sent message is returned,
            otherwise None.

        Example:
            .. code-block:: python

                await app.send_ephemeral_message(chat_id, "@mybot", "hello")
        """

        peer = await self.resolve_peer(chat_id)
        receiver_peer = await self.resolve_peer(receiver_id)
        if isinstance(receiver_peer, raw.types.InputPeerUser):
            receiver_peer = raw.types.InputUser(
                user_id=receiver_peer.user_id,
                access_hash=receiver_peer.access_hash
            )

        r = await self.invoke(
            raw.functions.ephemeral.SendMessage(
                peer=peer,
                receiver_id=receiver_peer,
                message=text,
                random_id=self.rnd_id(),
                query_id=query_id
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
