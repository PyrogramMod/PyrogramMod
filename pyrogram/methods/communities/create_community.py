from typing import Union, Optional

import pyrogram
from pyrogram import raw


class CreateCommunity:
    async def create_community(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        title: str,
        about: Optional[str] = None
    ) -> "raw.base.Updates":
        """Create a community linked to a channel or supergroup.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The channel or supergroup to link the community to.

            title (``str``):
                Community title.

            about (``str``, *optional*):
                Community description.

        Returns:
            :obj:`~pyrogram.raw.base.Updates`: On success.

        Example:
            .. code-block:: python

                await app.create_community(-100123456789, "My Community")
        """

        peer = await self.resolve_peer(chat_id)

        return await self.invoke(
            raw.functions.communities.Create(
                title=title,
                peer=peer,
                about=about
            )
        )
