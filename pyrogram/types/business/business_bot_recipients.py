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

from typing import List, Optional

import pyrogram
from pyrogram import raw, types
from ..object import Object


class BusinessBotRecipients(Object):
    """Represents recipients for a business bot.

    Parameters:
        existing_chats (``bool``, *optional*):
            True, if existing chats are included.

        new_chats (``bool``, *optional*):
            True, if new chats are included.

        contacts (``bool``, *optional*):
            True, if contacts are included.

        non_contacts (``bool``, *optional*):
            True, if non-contacts are included.

        exclude_selected (``bool``, *optional*):
            True, if selected users are excluded.

        users (List of ``int``, *optional*):
            List of included user IDs.

        exclude_users (List of ``int``, *optional*):
            List of excluded user IDs.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        existing_chats: bool = None,
        new_chats: bool = None,
        contacts: bool = None,
        non_contacts: bool = None,
        exclude_selected: bool = None,
        users: List[int] = None,
        exclude_users: List[int] = None
    ):
        super().__init__(client)

        self.existing_chats = existing_chats
        self.new_chats = new_chats
        self.contacts = contacts
        self.non_contacts = non_contacts
        self.exclude_selected = exclude_selected
        self.users = users
        self.exclude_users = exclude_users

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        recipients: "raw.types.BusinessBotRecipients"
    ) -> Optional["BusinessBotRecipients"]:
        if not recipients:
            return None

        return BusinessBotRecipients(
            client=client,
            existing_chats=recipients.existing_chats,
            new_chats=recipients.new_chats,
            contacts=recipients.contacts,
            non_contacts=recipients.non_contacts,
            exclude_selected=recipients.exclude_selected,
            users=types.List(recipients.users) if recipients.users else None,
            exclude_users=types.List(recipients.exclude_users) if recipients.exclude_users else None
        )
