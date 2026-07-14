import pyrogram
from pyrogram import raw


class GetJoinedCommunities:
    async def get_joined_communities(
        self: "pyrogram.Client"
    ) -> "raw.base.messages.Chats":
        """Get the list of communities the current user has joined.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            :obj:`~pyrogram.raw.base.messages.Chats`: List of community chats.

        Example:
            .. code-block:: python

                communities = await app.get_joined_communities()
        """

        return await self.invoke(raw.functions.communities.GetJoinedCommunities())
