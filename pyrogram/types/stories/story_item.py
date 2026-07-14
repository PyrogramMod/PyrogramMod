#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime
from typing import List, Optional, Union

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class StoryItem(Object):
    """Represents a story.

    Parameters:
        id (``int``):
            Unique identifier of the story.

        from_user (:obj:`~pyrogram.types.User`, *optional*):
            The user who posted this story.

        sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            The chat that posted this story (for channel stories).

        date (:py:obj:`~datetime.datetime`):
            When the story was posted.

        expire_date (:py:obj:`~datetime.datetime`):
            When the story will expire.

        caption (``str``, *optional*):
            Caption for the story.

        caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Special entities like usernames, URLs, etc. that appear in the caption.

        photo (:obj:`~pyrogram.types.Photo`, *optional*):
            Story photo, if the story contains a photo.

        video (:obj:`~pyrogram.types.Video`, *optional*):
            Story video, if the story contains a video.

        animation (:obj:`~pyrogram.types.Animation`, *optional*):
            Story animation, if the story contains an animation.

        views (:obj:`~pyrogram.types.StoryViews`, *optional*):
            View and reaction information.

        forward_from (:obj:`~pyrogram.types.StoryForwardHeader`, *optional*):
            For reposted stories, information about the original story.

        media_areas (List of :obj:`~pyrogram.types.MediaArea`, *optional*):
            Interactive areas on the story media.

        pinned (``bool``, *optional*):
            Whether this story is pinned on the user's profile.

        is_public (``bool``, *optional*):
            Whether this story is public and can be viewed by everyone.

        is_close_friends (``bool``, *optional*):
            Whether this story can only be viewed by close friends.

        is_contacts (``bool``, *optional*):
            Whether this story can only be viewed by contacts.

        is_selected_contacts (``bool``, *optional*):
            Whether this story can only be viewed by a select list of contacts.

        no_forwards (``bool``, *optional*):
            Whether this story is protected and cannot be forwarded.

        edited (``bool``, *optional*):
            Whether this story was edited.

        outgoing (``bool``, *optional*):
            Whether this is an outgoing story (posted by the current user).
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        from_user: "types.User" = None,
        sender_chat: "types.Chat" = None,
        date: datetime = None,
        expire_date: datetime = None,
        caption: str = None,
        caption_entities: List["types.MessageEntity"] = None,
        photo: "types.Photo" = None,
        video: "types.Video" = None,
        animation: "types.Animation" = None,
        views: "types.StoryViews" = None,
        forward_from: "types.StoryForwardHeader" = None,
        media_areas: List["types.MediaArea"] = None,
        pinned: bool = None,
        is_public: bool = None,
        is_close_friends: bool = None,
        is_contacts: bool = None,
        is_selected_contacts: bool = None,
        no_forwards: bool = None,
        edited: bool = None,
        outgoing: bool = None
    ):
        super().__init__(client)

        self.id = id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.date = date
        self.expire_date = expire_date
        self.caption = caption
        self.caption_entities = caption_entities
        self.photo = photo
        self.video = video
        self.animation = animation
        self.views = views
        self.forward_from = forward_from
        self.media_areas = media_areas
        self.pinned = pinned
        self.is_public = is_public
        self.is_close_friends = is_close_friends
        self.is_contacts = is_contacts
        self.is_selected_contacts = is_selected_contacts
        self.no_forwards = no_forwards
        self.edited = edited
        self.outgoing = outgoing

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        story: "raw.types.StoryItem",
        users: dict,
        chats: dict,
        peer: "raw.base.Peer" = None
    ) -> "StoryItem":
        from pyrogram.types.stories import StoryViews, StoryForwardHeader, MediaArea

        # Parse the peer (who posted the story)
        from_user = None
        sender_chat = None

        if peer:
            if isinstance(peer, raw.types.PeerUser):
                from_user = types.User._parse(client, users.get(peer.user_id))
            elif isinstance(peer, (raw.types.PeerChannel, raw.types.PeerChat)):
                peer_id = getattr(peer, "channel_id", None) or getattr(peer, "chat_id", None)
                sender_chat = types.Chat._parse_channel_chat(client, chats.get(peer_id))

        # If story has from_id, use that instead
        if story.from_id:
            if isinstance(story.from_id, raw.types.PeerUser):
                from_user = types.User._parse(client, users.get(story.from_id.user_id))
                sender_chat = None
            elif isinstance(story.from_id, raw.types.PeerChannel):
                sender_chat = types.Chat._parse_channel_chat(client, chats.get(story.from_id.channel_id))
                from_user = None

        # Parse media
        photo = None
        video = None
        animation = None

        if story.media:
            if isinstance(story.media, raw.types.MessageMediaPhoto):
                photo = types.Photo._parse(client, story.media.photo, story.media.ttl_seconds)
            elif isinstance(story.media, raw.types.MessageMediaDocument):
                doc = story.media.document
                if isinstance(doc, raw.types.Document):
                    attributes = {type(attr): attr for attr in doc.attributes}

                    if raw.types.DocumentAttributeAnimated in attributes:
                        video_attr = attributes.get(raw.types.DocumentAttributeVideo, None)
                        animation = types.Animation._parse(client, doc, video_attr, None)
                    elif raw.types.DocumentAttributeVideo in attributes:
                        video_attr = attributes[raw.types.DocumentAttributeVideo]
                        video = types.Video._parse(client, doc, video_attr, None, story.media.ttl_seconds)

        # Parse caption entities
        caption_entities = None
        if story.entities:
            caption_entities = types.List([
                types.MessageEntity._parse(client, entity, {})
                for entity in story.entities
            ])

        # Parse views
        views = None
        if story.views:
            views = StoryViews._parse(client, story.views)

        # Parse forward header
        forward_from = None
        if story.fwd_from:
            forward_from = StoryForwardHeader._parse(client, story.fwd_from)

        # Parse media areas
        media_areas = None
        if story.media_areas:
            parsed_areas = []
            for area in story.media_areas:
                parsed_area = MediaArea._parse(client, area)
                if parsed_area:
                    parsed_areas.append(parsed_area)
            if parsed_areas:
                media_areas = types.List(parsed_areas)

        return StoryItem(
            client=client,
            id=story.id,
            from_user=from_user,
            sender_chat=sender_chat,
            date=utils.timestamp_to_datetime(story.date),
            expire_date=utils.timestamp_to_datetime(story.expire_date),
            caption=story.caption or None,
            caption_entities=caption_entities,
            photo=photo,
            video=video,
            animation=animation,
            views=views,
            forward_from=forward_from,
            media_areas=media_areas,
            pinned=story.pinned or None,
            is_public=story.public or None,
            is_close_friends=story.close_friends or None,
            is_contacts=story.contacts or None,
            is_selected_contacts=story.selected_contacts or None,
            no_forwards=story.noforwards or None,
            edited=story.edited or None,
            outgoing=story.out or None
        )

    @property
    def chat(self) -> Union["types.Chat", "types.User"]:
        """The chat or user who posted this story."""
        return self.sender_chat or self.from_user

    async def delete(self) -> bool:
        """Bound method *delete* of :obj:`~pyrogram.types.StoryItem`.

        Use as a shortcut for:
            .. code-block:: python

                await story.delete()

        Returns:
            ``bool``: True on success.
        """
        return await self._client.delete_stories(
            chat_id=self.chat.id,
            story_ids=self.id
        )

    async def react(self, reaction: "types.Reaction" = None, add_to_recent: bool = None) -> bool:
        """Bound method *react* of :obj:`~pyrogram.types.StoryItem`.

        Use as a shortcut for:
            .. code-block:: python

                await story.react(reaction)

        Parameters:
            reaction (:obj:`~pyrogram.types.Reaction`, *optional*):
                The reaction to send.

            add_to_recent (``bool``, *optional*):
                Whether to add to recent reactions.

        Returns:
            ``bool``: True on success.
        """
        return await self._client.send_story_reaction(
            chat_id=self.chat.id,
            story_id=self.id,
            reaction=reaction,
            add_to_recent=add_to_recent
        )

    async def get_views(self, query: str = None, limit: int = 20) -> "types.StoryViewsList":
        """Bound method *get_views* of :obj:`~pyrogram.types.StoryItem`.

        Use as a shortcut for:
            .. code-block:: python

                await story.get_views()

        Parameters:
            query (``str``, *optional*):
                Search query.

            limit (``int``, *optional*):
                Maximum number of views to retrieve.

        Returns:
            :obj:`~pyrogram.types.StoryViewsList`: The list of views.
        """
        return await self._client.get_story_views_list(
            chat_id=self.chat.id,
            story_id=self.id,
            query=query,
            limit=limit
        )

    async def get_reactions(self, reaction: "types.Reaction" = None, limit: int = 20) -> "types.StoryReactionsList":
        """Bound method *get_reactions* of :obj:`~pyrogram.types.StoryItem`.

        Use as a shortcut for:
            .. code-block:: python

                await story.get_reactions()

        Parameters:
            reaction (:obj:`~pyrogram.types.Reaction`, *optional*):
                Filter by a specific reaction.

            limit (``int``, *optional*):
                Maximum number of reactions to retrieve.

        Returns:
            :obj:`~pyrogram.types.StoryReactionsList`: The list of reactions.
        """
        return await self._client.get_story_reactions_list(
            chat_id=self.chat.id,
            story_id=self.id,
            reaction=reaction,
            limit=limit
        )

    async def get_public_forwards(self, limit: int = 20) -> "types.PublicForwards":
        """Bound method *get_public_forwards* of :obj:`~pyrogram.types.StoryItem`.

        Use as a shortcut for:
            .. code-block:: python

                await story.get_public_forwards()

        Parameters:
            limit (``int``, *optional*):
                Maximum number of forwards to retrieve.

        Returns:
            :obj:`~pyrogram.types.PublicForwards`: The list of public forwards.
        """
        return await self._client.get_story_public_forwards(
            chat_id=self.chat.id,
            story_id=self.id,
            limit=limit
        )
