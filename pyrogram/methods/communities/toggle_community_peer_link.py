from typing import Union, Optional

import pyrogram
from pyrogram import raw


class ToggleCommunityPeerLink:
    async def toggle_community_peer_link(
        self: "pyrogram.Client",
        community_id: Union[int, str],
        peer_id: Union[int, str],
        visible: Optional[bool] = None,
        hidden: Optional[bool] = None,
        deleted: bool = False
    ) -> bool:
        """Toggle a peer link in a community (show, hide, or remove).

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            community_id (``int`` | ``str``):
                The community channel.

            peer_id (``int`` | ``str``):
                The peer to toggle.

            visible (``bool``, *optional*):
                Pass True to make the peer visible in the community.

            hidden (``bool``, *optional*):
                Pass True to hide the peer in the community.

            deleted (``bool``, *optional*):
                Pass True to remove the peer from the community.

        Returns:
            ``bool``: True on success.

        Raises:
            ~pyrogram.errors.PeerLinkNotModified: The peer is already in the
                requested state (e.g. already visible, already hidden, or
                already deleted).
            ~pyrogram.errors.ChatAdminRequired: The user is not an admin of
                the community.

        Example:
            .. code-block:: python

                await app.toggle_community_peer_link(community_id, peer_id, visible=True)
        """

        community = await self.resolve_peer(community_id)
        peer = await self.resolve_peer(peer_id)

        await self.invoke(
            raw.functions.communities.TogglePeerLink(
                community=community,
                peer=peer,
                visible=visible,
                hidden=hidden,
                deleted=deleted or None
            )
        )

        return True
