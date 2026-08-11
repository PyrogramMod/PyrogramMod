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
from typing import Optional

import pyrogram
from pyrogram import raw, utils
from pyrogram import types
from ..object import Object
from ..update import Update


class UserPhoto(Object, Update):
    """A user photo update.

    Parameters:
        user (:obj:`~pyrogram.types.User`):
            The user whose photo changed.

        date (:py:obj:`~datetime.datetime`):
            Date when the photo was updated.

        previous (``bool``):
            True if this was a previous photo.

        photo_id (``int``):
            The photo ID.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        user: "types.User",
        date: datetime,
        previous: bool = False,
        photo_id: int = 0,
    ):
        super().__init__(client)
        self.user = user
        self.date = date
        self.previous = previous
        self.photo_id = photo_id

    @staticmethod
    def _parse(client: "pyrogram.Client", update: "raw.types.UpdateUserPhoto", users: dict) -> "UserPhoto":
        user = types.User._parse(client, users.get(update.user_id))

        return UserPhoto(
            client=client,
            user=user,
            date=utils.timestamp_to_datetime(update.date),
            previous=update.previous,
            photo_id=update.photo.photo_id if update.photo else 0,
        )
