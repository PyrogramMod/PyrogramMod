from typing import Union

import pyrogram
from pyrogram import raw, utils


class EditEphemeralMessageMedia:
    async def edit_ephemeral_message_media(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        receiver_id: Union[int, str],
        ephemeral_message_id: int,
        file_id: str,
        reply_markup=None
    ) -> "raw.base.Updates":
        """Edit the media of an ephemeral message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context (chat) the ephemeral message belongs to.

            receiver_id (``int`` | ``str``):
                The bot user that received the ephemeral message.

            ephemeral_message_id (``int``):
                Identifier of the ephemeral message to edit.

            file_id (``str``):
                New media, as a file_id of media already on the Telegram servers.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An inline keyboard.

        Returns:
            :obj:`~pyrogram.raw.base.Updates`: On success.

        Example:
            .. code-block:: python

                await app.edit_ephemeral_message_media(chat_id, "@mybot", 123, file_id)
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
                media=utils.get_input_media_from_file_id(file_id),
                reply_markup=await reply_markup.write(self) if reply_markup else None
            )
        )
