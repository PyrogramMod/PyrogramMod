from typing import Union

import pyrogram
from pyrogram import raw


class GetCommunityPeerLinkRequests:
    async def get_community_peer_link_requests(
        self: "pyrogram.Client",
        community_id: Union[int, str],
        offset: str = "",
        limit: int = 100
    ) -> "raw.base.PeerLinkRequests":
        """Get pending peer link requests for a community.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            community_id (``int`` | ``str``):
                The community channel.

            offset (``str``, *optional*):
                Pagination offset. Defaults to empty string (start from beginning).

            limit (``int``, *optional*):
                Maximum number of results. Defaults to 100.

        Returns:
            :obj:`~pyrogram.raw.base.PeerLinkRequests`: The pending requests.

        Example:
            .. code-block:: python

                requests = await app.get_community_peer_link_requests(community_id)
        """

        community = await self.resolve_peer(community_id)

        return await self.invoke(
            raw.functions.communities.GetPeerLinkRequests(
                community=community,
                offset=offset,
                limit=limit
            )
        )
