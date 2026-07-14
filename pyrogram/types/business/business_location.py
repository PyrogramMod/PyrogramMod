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

from typing import Optional

import pyrogram
from pyrogram import raw, types
from ..object import Object


class BusinessLocation(Object):
    """Represents the location of a business.

    Parameters:
        address (``str``):
            Text address of the business location.

        geo (:obj:`~pyrogram.types.Location`, *optional*):
            Geographic coordinates of the location.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        address: str,
        geo: "types.Location" = None
    ):
        super().__init__(client)

        self.address = address
        self.geo = geo

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        location: "raw.types.BusinessLocation"
    ) -> Optional["BusinessLocation"]:
        if location is None:
            return None

        geo = None
        if location.geo_point and isinstance(location.geo_point, raw.types.GeoPoint):
            geo = types.Location(
                longitude=location.geo_point.long,
                latitude=location.geo_point.lat,
                client=client
            )

        return BusinessLocation(
            client=client,
            address=location.address,
            geo=geo
        )
