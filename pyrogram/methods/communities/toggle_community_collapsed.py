from typing import Union, Optional

import pyrogram
from pyrogram import raw


class ToggleCommunityCollapsed:
    async def toggle_community_collapsed(
        self: "pyrogram.Client",
        community_id: Union[int, str],
        collapsed: Optional[bool] = None
    ) -> bool:
        """Toggle whether a community is collapsed in the dialogs list.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            community_id (``int`` | ``str``):
                The community channel.

            collapsed (``bool``, *optional*):
                Pass True to collapse, False to expand.

        Returns:
            ``bool``: True on success.

        Raises:
            ~pyrogram.errors.ChatAdminRequired: The user is not an admin of
                the community.

        Example:
            .. code-block:: python

                await app.toggle_community_collapsed(community_id, collapsed=True)
        """

        community = await self.resolve_peer(community_id)

        await self.invoke(
            raw.functions.communities.ToggleCommunityCollapsedInDialogs(
                community=community,
                collapsed=collapsed
            )
        )

        return True
