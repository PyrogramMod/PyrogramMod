from typing import Union

import pyrogram
from pyrogram import raw


class ApproveAllCommunityPeerLinks:
    async def approve_all_community_peer_links(
        self: "pyrogram.Client",
        community_id: Union[int, str],
        reject: bool = False
    ) -> bool:
        """Approve or reject all pending peer link requests in a community.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            community_id (``int`` | ``str``):
                The community channel.

            reject (``bool``, *optional*):
                Pass True to reject all instead of approving. Defaults to False.

        Returns:
            ``bool``: True on success.

        Raises:
            ~pyrogram.errors.ChatAdminRequired: The user is not an admin of
                the community.

        Example:
            .. code-block:: python

                await app.approve_all_community_peer_links(community_id)
        """

        community = await self.resolve_peer(community_id)

        await self.invoke(
            raw.functions.communities.ToggleAllPeerLinkRequestApproval(
                community=community,
                reject=reject or None
            )
        )

        return True
