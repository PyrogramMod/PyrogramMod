from typing import Union, Optional

import pyrogram
from pyrogram import raw


class ApproveCommunityPeerLink:
    async def approve_community_peer_link(
        self: "pyrogram.Client",
        community_id: Union[int, str],
        peer_id: Union[int, str],
        reject: bool = False
    ) -> bool:
        """Approve or reject a peer link request in a community.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            community_id (``int`` | ``str``):
                The community channel.

            peer_id (``int`` | ``str``):
                The peer whose request to approve or reject.

            reject (``bool``, *optional*):
                Pass True to reject instead of approving. Defaults to False.

        Returns:
            ``bool``: True on success.

        Raises:
            ~pyrogram.errors.ChatAdminRequired: The user is not an admin of
                the community.

        Example:
            .. code-block:: python

                await app.approve_community_peer_link(community_id, peer_id)
                await app.approve_community_peer_link(community_id, peer_id, reject=True)
        """

        community = await self.resolve_peer(community_id)
        peer = await self.resolve_peer(peer_id)

        await self.invoke(
            raw.functions.communities.TogglePeerLinkRequestApproval(
                community=community,
                peer=peer,
                reject=reject or None
            )
        )

        return True
