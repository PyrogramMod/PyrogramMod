from typing import Union

import pyrogram
from pyrogram import raw


class DeleteEphemeralMessage:
    async def delete_ephemeral_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        receiver_id: Union[int, str],
        message_id: int
    ) -> bool:
        """Delete an ephemeral message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context of the ephemeral message.

            receiver_id (``int`` | ``str``):
                The receiver bot of the ephemeral message.

            message_id (``int``):
                The ID of the ephemeral message to delete.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.delete_ephemeral_message(chat_id, "@mybot", 123)
        """

        peer = await self.resolve_peer(chat_id)
        receiver_peer = await self.resolve_peer(receiver_id)
        if isinstance(receiver_peer, raw.types.InputPeerUser):
            receiver_peer = raw.types.InputUser(
                user_id=receiver_peer.user_id,
                access_hash=receiver_peer.access_hash
            )

        return await self.invoke(
            raw.functions.ephemeral.DeleteMessage(
                peer=peer,
                receiver_id=receiver_peer,
                id=message_id
            )
        )
