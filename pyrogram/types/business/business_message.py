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
from pyrogram import raw, types, utils
from ..object import Object


class BusinessRecipients(Object):
    """Represents recipients for business automated messages.

    Parameters:
        existing_chats (``bool``, *optional*):
            Apply to existing private chats.

        new_chats (``bool``, *optional*):
            Apply to new private chats.

        contacts (``bool``, *optional*):
            Apply to contacts.

        non_contacts (``bool``, *optional*):
            Apply to non-contacts.

        exclude_selected (``bool``, *optional*):
            If True, the users/chats below are excluded rather than included.

        users (List of ``int``, *optional*):
            List of user IDs to include/exclude.
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
        users: List[int] = None
    ):
        super().__init__(client)

        self.existing_chats = existing_chats
        self.new_chats = new_chats
        self.contacts = contacts
        self.non_contacts = non_contacts
        self.exclude_selected = exclude_selected
        self.users = users

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        recipients: "raw.types.BusinessRecipients"
    ) -> Optional["BusinessRecipients"]:
        if recipients is None:
            return None

        users = None
        if recipients.users:
            users = types.List(recipients.users)

        return BusinessRecipients(
            client=client,
            existing_chats=recipients.existing_chats or None,
            new_chats=recipients.new_chats or None,
            contacts=recipients.contacts or None,
            non_contacts=recipients.non_contacts or None,
            exclude_selected=recipients.exclude_selected or None,
            users=users
        )


class BusinessGreetingMessage(Object):
    """Represents an automated greeting message for business accounts.

    Parameters:
        shortcut_id (``int``):
            ID of the quick reply shortcut containing the message.

        recipients (:obj:`~pyrogram.types.BusinessRecipients`):
            Recipients who will receive this greeting.

        no_activity_days (``int``):
            Number of days of inactivity after which the greeting is sent.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        shortcut_id: int,
        recipients: "BusinessRecipients" = None,
        no_activity_days: int = None
    ):
        super().__init__(client)

        self.shortcut_id = shortcut_id
        self.recipients = recipients
        self.no_activity_days = no_activity_days

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        message: "raw.types.BusinessGreetingMessage"
    ) -> Optional["BusinessGreetingMessage"]:
        if message is None:
            return None

        return BusinessGreetingMessage(
            client=client,
            shortcut_id=message.shortcut_id,
            recipients=BusinessRecipients._parse(client, message.recipients),
            no_activity_days=message.no_activity_days
        )


class BusinessAwayMessage(Object):
    """Represents an automated away message for business accounts.

    Parameters:
        shortcut_id (``int``):
            ID of the quick reply shortcut containing the message.

        recipients (:obj:`~pyrogram.types.BusinessRecipients`):
            Recipients who will receive this away message.

        schedule_type (``str``):
            Type of schedule. One of: "always", "outside_work_hours", "custom".

        offline_only (``bool``, *optional*):
            Only send when the account is offline.

        start_date (:py:obj:`~datetime.datetime`, *optional*):
            For "custom" schedule: start date.

        end_date (:py:obj:`~datetime.datetime`, *optional*):
            For "custom" schedule: end date.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        shortcut_id: int,
        recipients: "BusinessRecipients" = None,
        schedule_type: str = None,
        offline_only: bool = None,
        start_date: "datetime" = None,
        end_date: "datetime" = None
    ):
        super().__init__(client)

        self.shortcut_id = shortcut_id
        self.recipients = recipients
        self.schedule_type = schedule_type
        self.offline_only = offline_only
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        message: "raw.types.BusinessAwayMessage"
    ) -> Optional["BusinessAwayMessage"]:
        if message is None:
            return None

        schedule_type = "always"
        start_date = None
        end_date = None

        if isinstance(message.schedule, raw.types.BusinessAwayMessageScheduleAlways):
            schedule_type = "always"
        elif isinstance(message.schedule, raw.types.BusinessAwayMessageScheduleOutsideWorkHours):
            schedule_type = "outside_work_hours"
        elif isinstance(message.schedule, raw.types.BusinessAwayMessageScheduleCustom):
            schedule_type = "custom"
            start_date = utils.timestamp_to_datetime(message.schedule.start_date)
            end_date = utils.timestamp_to_datetime(message.schedule.end_date)

        return BusinessAwayMessage(
            client=client,
            shortcut_id=message.shortcut_id,
            recipients=BusinessRecipients._parse(client, message.recipients),
            schedule_type=schedule_type,
            offline_only=message.offline_only or None,
            start_date=start_date,
            end_date=end_date
        )
