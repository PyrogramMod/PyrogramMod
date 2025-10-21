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

import html
from datetime import datetime
from typing import List, Optional

import pyrogram
from pyrogram import enums, utils
from pyrogram import raw
from pyrogram import types
from ..object import Object
from ..update import Update


class Link(str):
    HTML = "<a href={url}>{text}</a>"
    MARKDOWN = "[{text}]({url})"

    def __init__(self, url: str, text: str, style: enums.ParseMode):
        super().__init__()

        self.url = url
        self.text = text
        self.style = style

    @staticmethod
    def format(url: str, text: str, style: enums.ParseMode):
        if style == enums.ParseMode.MARKDOWN:
            fmt = Link.MARKDOWN
        else:
            fmt = Link.HTML

        return fmt.format(url=url, text=html.escape(text))

    # noinspection PyArgumentList
    def __new__(cls, url, text, style):
        return str.__new__(cls, Link.format(url, text, style))

    def __call__(self, other: str = None, *, style: str = None):
        return Link.format(self.url, other or self.text, style or self.style)

    def __str__(self):
        return Link.format(self.url, self.text, self.style)


class User(Object, Update):
    """A Telegram user or bot.

    Parameters:
        id (``int``):
            Unique identifier for this user or bot.

        is_self(``bool``, *optional*):
            True, if this user is you yourself.

        is_contact(``bool``, *optional*):
            True, if this user is in your contacts.

        is_mutual_contact(``bool``, *optional*):
            True, if you both have each other's contact.

        is_deleted(``bool``, *optional*):
            True, if this user is deleted.

        is_bot (``bool``, *optional*):
            True, if this user is a bot.

        is_verified (``bool``, *optional*):
            True, if this user has been verified by Telegram.

        is_restricted (``bool``, *optional*):
            True, if this user has been restricted. Bots only.
            See *restriction_reason* for details.

        is_scam (``bool``, *optional*):
            True, if this user has been flagged for scam.

        is_fake (``bool``, *optional*):
            True, if this user has been flagged for impersonation.

        is_support (``bool``, *optional*):
            True, if this user is part of the Telegram support team.

        is_premium (``bool``, *optional*):
            True, if this user is a premium user.

        first_name (``str``, *optional*):
            User's or bot's first name.

        last_name (``str``, *optional*):
            User's or bot's last name.

        status (:obj:`~pyrogram.enums.UserStatus`, *optional*):
            User's last seen & online status. ``None``, for bots.

        last_online_date (:py:obj:`~datetime.datetime`, *optional*):
            Last online date of a user. Only available in case status is :obj:`~pyrogram.enums.UserStatus.OFFLINE`.

        next_offline_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when a user will automatically go offline. Only available in case status is :obj:`~pyrogram.enums.UserStatus.ONLINE`.

        username (``str``, *optional*):
            User's or bot's username.

        language_code (``str``, *optional*):
            IETF language tag of the user's language.

        emoji_status (:obj:`~pyrogram.types.EmojiStatus`, *optional*):
            Emoji status.

        dc_id (``int``, *optional*):
            User's or bot's assigned DC (data center). Available only in case the user has set a public profile photo.
            Note that this information is approximate; it is based on where Telegram stores a user profile pictures and
            does not by any means tell you the user location (i.e. a user might travel far away, but will still connect
            to its assigned DC). More info at `FAQs </faq#what-are-the-ip-addresses-of-telegram-data-centers>`_.

        phone_number (``str``, *optional*):
            User's phone number.

        photo (:obj:`~pyrogram.types.ChatPhoto`, *optional*):
            User's or bot's current profile photo. Suitable for downloads only.

        restrictions (List of :obj:`~pyrogram.types.Restriction`, *optional*):
            The list of reasons why this bot might be unavailable to some users.
            This field is available only in case *is_restricted* is True.

        full_name (``str``, *optional*):
            User's or bot's full name.

        mention (``str``, *property*):
            Generate a text mention for this user.
            You can use ``user.mention()`` to mention the user using their first name (styled using html), or
            ``user.mention("another name")`` for a custom name. To choose a different style
            ("html" or "md"/"markdown") use ``user.mention(style="md")``.

        usernames (List of :obj:`~pyrogram.types.Username`, *optional*):
            The list of user's collectible (and basic) usernames if availables.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        is_self: bool = None,
        is_contact: bool = None,
        is_mutual_contact: bool = None,
        is_deleted: bool = None,
        is_bot: bool = None,
        is_verified: bool = None,
        is_restricted: bool = None,
        is_scam: bool = None,
        is_fake: bool = None,
        is_support: bool = None,
        is_premium: bool = None,
        first_name: str = None,
        last_name: str = None,
        status: "enums.UserStatus" = None,
        last_online_date: datetime = None,
        next_offline_date: datetime = None,
        username: str = None,
        language_code: str = None,
        emoji_status: Optional["types.EmojiStatus"] = None,
        dc_id: int = None,
        phone_number: str = None,
        photo: "types.ChatPhoto" = None,
        restrictions: List["types.Restriction"] = None,
        usernames: List["types.Username"] = None,
        bot_chat_history: bool = None,
        bot_nochats: bool = None,
        bot_inline_geo: bool = None,
        apply_min_photo: bool = None,
        bot_attach_menu: bool = None,
        attach_menu_enabled: bool = None,
        bot_can_edit: bool = None,
        close_friend: bool = None,
        stories_hidden: bool = None,
        stories_unavailable: bool = None,
        contact_require_premium: bool = None,
        bot_business: bool = None,
        bot_has_main_app: bool = None,
        bot_forum_view: bool = None,
        access_hash: int = None,
        bot_info_version: int = None,
        bot_inline_placeholder: str = None,
        stories_max_id: int = None,
        color: "types.PeerColor" = None,
        profile_color: "types.PeerColor" = None,
        bot_active_users: int = None,
        bot_verification_icon: int = None,
        send_paid_messages_stars: int = None,
        restriction_reason: List["types.Restriction"] = None
    ):
        super().__init__(client)

        self.id = id
        self.is_self = is_self
        self.is_contact = is_contact
        self.is_mutual_contact = is_mutual_contact
        self.is_deleted = is_deleted
        self.is_bot = is_bot
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_support = is_support
        self.is_premium = is_premium
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.last_online_date = last_online_date
        self.next_offline_date = next_offline_date
        self.username = username
        self.language_code = language_code
        self.emoji_status = emoji_status
        self.dc_id = dc_id
        self.phone_number = phone_number
        self.photo = photo
        self.restrictions = restrictions
        self.usernames = usernames
        self.bot_chat_history = bot_chat_history
        self.bot_nochats = bot_nochats
        self.bot_inline_geo = bot_inline_geo
        self.apply_min_photo = apply_min_photo
        self.bot_attach_menu = bot_attach_menu
        self.attach_menu_enabled = attach_menu_enabled
        self.bot_can_edit = bot_can_edit
        self.close_friend = close_friend
        self.stories_hidden = stories_hidden
        self.stories_unavailable = stories_unavailable
        self.contact_require_premium = contact_require_premium
        self.bot_business = bot_business
        self.bot_has_main_app = bot_has_main_app
        self.bot_forum_view = bot_forum_view
        self.access_hash = access_hash
        self.bot_info_version = bot_info_version
        self.bot_inline_placeholder = bot_inline_placeholder
        self.stories_max_id = stories_max_id
        self.color = color
        self.profile_color = profile_color
        self.bot_active_users = bot_active_users
        self.bot_verification_icon = bot_verification_icon
        self.send_paid_messages_stars = send_paid_messages_stars
        self.restriction_reason = restriction_reason or restrictions

    @property
    def full_name(self) -> str:
        return " ".join(filter(None, [self.first_name, self.last_name])) or None

    @property
    def mention(self):
        return Link(
            f"tg://user?id={self.id}",
            self.first_name or "Deleted Account",
            self._client.parse_mode
        )

    @staticmethod
    def _parse(client, user: "raw.base.User") -> Optional["User"]:
        if user is None or isinstance(user, raw.types.UserEmpty):
            return None

        parsed_restrictions = types.List([types.Restriction._parse(r) for r in user.restriction_reason]) or None

        return User(
            id=user.id,
            is_self=user.is_self,
            is_contact=user.contact,
            is_mutual_contact=user.mutual_contact,
            is_deleted=user.deleted,
            is_bot=user.bot,
            is_verified=user.verified,
            is_restricted=user.restricted,
            is_scam=user.scam,
            is_fake=user.fake,
            is_support=user.support,
            is_premium=user.premium,
            first_name=user.first_name,
            last_name=user.last_name,
            **User._parse_status(user.status, user.bot),
            username=user.username,
            language_code=user.lang_code,
            emoji_status=types.EmojiStatus._parse(client, user.emoji_status),
            dc_id=getattr(user.photo, "dc_id", None),
            phone_number=user.phone,
            photo=types.ChatPhoto._parse(client, user.photo, user.id, user.access_hash),
            restrictions=parsed_restrictions,
            restriction_reason=parsed_restrictions,
            usernames=types.List([types.Username._parse(r) for r in user.usernames]) or None,
            bot_chat_history=getattr(user, "bot_chat_history", None),
            bot_nochats=getattr(user, "bot_nochats", None),
            bot_inline_geo=getattr(user, "bot_inline_geo", None),
            apply_min_photo=getattr(user, "apply_min_photo", None),
            bot_attach_menu=getattr(user, "bot_attach_menu", None),
            attach_menu_enabled=getattr(user, "attach_menu_enabled", None),
            bot_can_edit=getattr(user, "bot_can_edit", None),
            close_friend=getattr(user, "close_friend", None),
            stories_hidden=getattr(user, "stories_hidden", None),
            stories_unavailable=getattr(user, "stories_unavailable", None),
            contact_require_premium=getattr(user, "contact_require_premium", None),
            bot_business=getattr(user, "bot_business", None),
            bot_has_main_app=getattr(user, "bot_has_main_app", None),
            bot_forum_view=getattr(user, "bot_forum_view", None),
            access_hash=getattr(user, "access_hash", None),
            bot_info_version=getattr(user, "bot_info_version", None),
            bot_inline_placeholder=getattr(user, "bot_inline_placeholder", None),
            stories_max_id=getattr(user, "stories_max_id", None),
            color=types.PeerColor._parse(getattr(user, "color", None)),
            profile_color=types.PeerColor._parse(getattr(user, "profile_color", None)),
            bot_active_users=getattr(user, "bot_active_users", None),
            bot_verification_icon=getattr(user, "bot_verification_icon", None),
            send_paid_messages_stars=getattr(user, "send_paid_messages_stars", None),
            client=client
        )

    @staticmethod
    def _parse_status(user_status: "raw.base.UserStatus", is_bot: bool = False):
        if isinstance(user_status, raw.types.UserStatusOnline):
            status, date = enums.UserStatus.ONLINE, user_status.expires
        elif isinstance(user_status, raw.types.UserStatusOffline):
            status, date = enums.UserStatus.OFFLINE, user_status.was_online
        elif isinstance(user_status, raw.types.UserStatusRecently):
            status, date = enums.UserStatus.RECENTLY, None
        elif isinstance(user_status, raw.types.UserStatusLastWeek):
            status, date = enums.UserStatus.LAST_WEEK, None
        elif isinstance(user_status, raw.types.UserStatusLastMonth):
            status, date = enums.UserStatus.LAST_MONTH, None
        else:
            status, date = enums.UserStatus.LONG_AGO, None

        last_online_date = None
        next_offline_date = None

        if is_bot:
            status = None

        if status == enums.UserStatus.ONLINE:
            next_offline_date = utils.timestamp_to_datetime(date)

        if status == enums.UserStatus.OFFLINE:
            last_online_date = utils.timestamp_to_datetime(date)

        return {
            "status": status,
            "last_online_date": last_online_date,
            "next_offline_date": next_offline_date
        }

    @staticmethod
    def _parse_user_status(client, user_status: "raw.types.UpdateUserStatus"):
        return User(
            id=user_status.user_id,
            **User._parse_status(user_status.status),
            client=client
        )

    async def archive(self):
        """Bound method *archive* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            await client.archive_chats(123456789)

        Example:
            .. code-block:: python

               await user.archive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.archive_chats(self.id)

    async def unarchive(self):
        """Bound method *unarchive* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            await client.unarchive_chats(123456789)

        Example:
            .. code-block:: python

                await user.unarchive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.unarchive_chats(self.id)

    def block(self):
        """Bound method *block* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            await client.block_user(123456789)

        Example:
            .. code-block:: python

                await user.block()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return self._client.block_user(self.id)

    def unblock(self):
        """Bound method *unblock* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            client.unblock_user(123456789)

        Example:
            .. code-block:: python

                user.unblock()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return self._client.unblock_user(self.id)

    def get_common_chats(self):
        """Bound method *get_common_chats* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            client.get_common_chats(123456789)

        Example:
            .. code-block:: python

                user.get_common_chats()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return self._client.get_common_chats(self.id)
