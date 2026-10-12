import pyrogram
from pyrogram import raw
from pyrogram import types


class GetJoinedCommunities:
    async def get_joined_communities(
        self: "pyrogram.Client"
    ) -> "types.List":
        """Get the list of communities the current user has joined.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            :obj:`~pyrogram.types.List` of :obj:`~pyrogram.types.Chat`: List of community chats.

        Example:
            .. code-block:: python

                communities = await app.get_joined_communities()
                for chat in communities:
                    print(chat.title)
        """

        r = await self.invoke(raw.functions.communities.GetJoinedCommunities())

        chats = types.List()

        for chat in r.chats:
            if isinstance(chat, raw.types.Chat):
                chats.append(types.Chat._parse_chat_chat(self, chat))
            elif isinstance(chat, raw.types.Channel):
                chats.append(types.Chat._parse_channel_chat(self, chat))

        return chats
