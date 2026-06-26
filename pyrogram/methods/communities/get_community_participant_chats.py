from typing import Union

import pyrogram
from pyrogram import raw


class GetCommunityParticipantChats:
    async def get_community_participant_chats(
        self: "pyrogram.Client",
        community_id: Union[int, str],
        participant_id: Union[int, str]
    ) -> "raw.base.ParticipantJoinedChats":
        """Get chats joined by a participant in a community.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            community_id (``int`` | ``str``):
                The community channel.

            participant_id (``int`` | ``str``):
                The participant.

        Returns:
            :obj:`~pyrogram.raw.base.ParticipantJoinedChats`: Chats the participant joined.

        Example:
            .. code-block:: python

                result = await app.get_community_participant_chats(community_id, user_id)
        """

        community = await self.resolve_peer(community_id)
        participant = await self.resolve_peer(participant_id)

        return await self.invoke(
            raw.functions.communities.GetParticipantJoinedChats(
                community=community,
                participant=participant
            )
        )
