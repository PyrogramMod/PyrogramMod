from typing import Union

import pyrogram
from pyrogram import raw


class ReportEphemeralMessage:
    async def report_ephemeral_message(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        option: bytes,
        message: str = ""
    ) -> "raw.base.ReportResult":
        """Report an ephemeral message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The peer context of the ephemeral message.

            message_id (``int``):
                The ephemeral message ID.

            option (``bytes``):
                Report option bytes.

            message (``str``, *optional*):
                Additional report comment. Defaults to empty string.

        Returns:
            :obj:`~pyrogram.raw.base.ReportResult`: The report result.

        Example:
            .. code-block:: python

                await app.report_ephemeral_message(chat_id, 123, b"\\x00", "spam")
        """

        peer = await self.resolve_peer(chat_id)

        return await self.invoke(
            raw.functions.ephemeral.ReportMessage(
                peer=peer,
                id=message_id,
                option=option,
                message=message
            )
        )
