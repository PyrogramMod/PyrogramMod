from typing import Union

import pyrogram
from pyrogram import raw


class EditEphemeralMessageReplyMarkup:
    async def edit_ephemeral_message_reply_markup(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        receiver_id: Union[int, str],
        ephemeral_message_id: int,
        reply_markup=None
    ) -> "raw.base.Updates":
        """Edit only the reply markup of an ephemeral message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context (chat) the ephemeral message belongs to.

            receiver_id (``int`` | ``str``):
                The bot user that received the ephemeral message.

            ephemeral_message_id (``int``):
                Identifier of the ephemeral message to edit.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An inline keyboard. Pass None to remove it.

        Returns:
            :obj:`~pyrogram.raw.base.Updates`: On success.

        Example:
            .. code-block:: python

                await app.edit_ephemeral_message_reply_markup(chat_id, "@mybot", 123, new_markup)
        """
        receiver_peer = await self.resolve_peer(receiver_id)
        if isinstance(receiver_peer, raw.types.InputPeerUser):
            receiver_peer = raw.types.InputUser(
                user_id=receiver_peer.user_id,
                access_hash=receiver_peer.access_hash
            )

        return await self.invoke(
            raw.functions.ephemeral.EditMessage(
                peer=await self.resolve_peer(chat_id),
                receiver_id=receiver_peer,
                id=ephemeral_message_id,
                reply_markup=await reply_markup.write(self) if reply_markup else None
            )
        )
