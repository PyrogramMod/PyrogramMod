from typing import Union

import pyrogram
from pyrogram import raw


class BanCommunityParticipant:
    async def ban_community_participant(
        self: "pyrogram.Client",
        community_id: Union[int, str],
        participant_id: Union[int, str],
        unban: bool = False
    ) -> bool:
        """Ban or unban a participant in a community.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            community_id (``int`` | ``str``):
                The community channel.

            participant_id (``int`` | ``str``):
                The participant to ban or unban.

            unban (``bool``, *optional*):
                Pass True to unban. Defaults to False.

        Returns:
            ``bool``: True on success.

        Example:
            .. code-block:: python

                await app.ban_community_participant(community_id, user_id)
                await app.ban_community_participant(community_id, user_id, unban=True)
        """

        community = await self.resolve_peer(community_id)
        participant = await self.resolve_peer(participant_id)

        await self.invoke(
            raw.functions.communities.ToggleParticipantBanned(
                community=community,
                participant=participant,
                unban=unban or None
            )
        )

        return True
