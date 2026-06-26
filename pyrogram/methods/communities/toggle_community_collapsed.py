from typing import Union, Optional

import pyrogram
from pyrogram import raw


class ToggleCommunityCollapsed:
    async def toggle_community_collapsed(
        self: "pyrogram.Client",
        community_id: Union[int, str],
        collapsed: Optional[bool] = None
    ) -> "raw.base.Updates":
        """Toggle whether a community is collapsed in the dialogs list.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            community_id (``int`` | ``str``):
                The community channel.

            collapsed (``bool``, *optional*):
                Pass True to collapse, False to expand.

        Returns:
            :obj:`~pyrogram.raw.base.Updates`: On success.

        Example:
            .. code-block:: python

                await app.toggle_community_collapsed(community_id, collapsed=True)
        """

        community = await self.resolve_peer(community_id)

        return await self.invoke(
            raw.functions.communities.ToggleCommunityCollapsedInDialogs(
                community=community,
                collapsed=collapsed
            )
        )
