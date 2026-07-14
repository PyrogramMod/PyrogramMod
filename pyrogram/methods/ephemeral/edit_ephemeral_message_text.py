from typing import Union, List, Optional

import pyrogram
from pyrogram import raw, utils, enums


class EditEphemeralMessageText:
    async def edit_ephemeral_message_text(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        receiver_id: Union[int, str],
        ephemeral_message_id: int,
        text: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        entities: Optional[List["pyrogram.types.MessageEntity"]] = None,
        reply_markup=None
    ) -> "raw.base.Updates":
        """Edit the text of an ephemeral message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context (chat) the ephemeral message belongs to.

            receiver_id (``int`` | ``str``):
                The bot user that received the ephemeral message.

            ephemeral_message_id (``int``):
                Identifier of the ephemeral message to edit.

            text (``str``):
                New message text.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.

            entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
                List of special entities that appear in message text, which can be specified instead of *parse_mode*.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An inline keyboard.

        Returns:
            :obj:`~pyrogram.raw.base.Updates`: On success.

        Example:
            .. code-block:: python

                await app.edit_ephemeral_message_text(chat_id, "@mybot", 123, "new text")
        """
        message, entities = (await utils.parse_text_entities(self, text, parse_mode, entities)).values()

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
                message=message,
                entities=entities,
                reply_markup=await reply_markup.write(self) if reply_markup else None
            )
        )
