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
from pyrogram import raw
from ..object import Object


class MediaAreaCoordinates(Object):
    """Coordinates and size of a clickable rectangular area on top of a story.

    Parameters:
        x (``float``):
            The abscissa of the rectangle's center, as a percentage of the media width (0-100).

        y (``float``):
            The ordinate of the rectangle's center, as a percentage of the media height (0-100).

        width (``float``):
            The width of the rectangle, as a percentage of the media width (0-100).

        height (``float``):
            The height of the rectangle, as a percentage of the media height (0-100).

        rotation (``float``):
            Clockwise rotation angle of the rectangle, in degrees (0-360).

        radius (``float``, *optional*):
            The radius of the rectangle corner rounding, as a percentage of the media width.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        x: float,
        y: float,
        width: float,
        height: float,
        rotation: float,
        radius: float = None
    ):
        super().__init__(client)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation
        self.radius = radius

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        coordinates: "raw.types.MediaAreaCoordinates"
    ) -> "MediaAreaCoordinates":
        return MediaAreaCoordinates(
            client=client,
            x=coordinates.x,
            y=coordinates.y,
            width=coordinates.w,
            height=coordinates.h,
            rotation=coordinates.rotation,
            radius=coordinates.radius
        )


class MediaArea(Object):
    """Represents a clickable rectangular area on a story.

    Parameters:
        coordinates (:obj:`~pyrogram.types.MediaAreaCoordinates`):
            The coordinates of this area.

        type (``str``):
            Type of the media area. Can be one of:
            - "geo": A location
            - "venue": A venue
            - "reaction": A suggested reaction
            - "channel_post": A channel post
            - "url": A URL
            - "weather": Weather information
            - "star_gift": A star gift

        geo (:obj:`~pyrogram.types.Location`, *optional*):
            For "geo" type, the location.

        venue (:obj:`~pyrogram.types.Venue`, *optional*):
            For "venue" type, the venue.

        reaction (:obj:`~pyrogram.types.Reaction`, *optional*):
            For "reaction" type, the suggested reaction.

        channel_id (``int``, *optional*):
            For "channel_post" type, the channel ID.

        message_id (``int``, *optional*):
            For "channel_post" type, the message ID.

        url (``str``, *optional*):
            For "url" type, the URL.

        is_dark (``bool``, *optional*):
            For "reaction" type, whether it should be displayed in dark mode.

        is_flipped (``bool``, *optional*):
            For "reaction" type, whether the reaction is flipped.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        coordinates: "MediaAreaCoordinates" = None,
        type: str = None,
        geo: "pyrogram.types.Location" = None,
        venue: "pyrogram.types.Venue" = None,
        reaction: "pyrogram.types.Reaction" = None,
        channel_id: int = None,
        message_id: int = None,
        url: str = None,
        is_dark: bool = None,
        is_flipped: bool = None
    ):
        super().__init__(client)

        self.coordinates = coordinates
        self.type = type
        self.geo = geo
        self.venue = venue
        self.reaction = reaction
        self.channel_id = channel_id
        self.message_id = message_id
        self.url = url
        self.is_dark = is_dark
        self.is_flipped = is_flipped

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        media_area: "raw.base.MediaArea"
    ) -> Optional["MediaArea"]:
        from pyrogram import types

        if isinstance(media_area, raw.types.MediaAreaGeoPoint):
            geo = None
            if isinstance(media_area.geo, raw.types.GeoPoint):
                geo = types.Location(
                    longitude=media_area.geo.long,
                    latitude=media_area.geo.lat,
                    client=client
                )
            return MediaArea(
                client=client,
                coordinates=MediaAreaCoordinates._parse(client, media_area.coordinates),
                type="geo",
                geo=geo
            )
        elif isinstance(media_area, raw.types.MediaAreaVenue):
            venue = types.Venue(
                location=types.Location(
                    longitude=media_area.geo.long if isinstance(media_area.geo, raw.types.GeoPoint) else 0,
                    latitude=media_area.geo.lat if isinstance(media_area.geo, raw.types.GeoPoint) else 0,
                    client=client
                ),
                title=media_area.title,
                address=media_area.address,
                foursquare_id=media_area.venue_id if media_area.provider == "foursquare" else None,
                foursquare_type=media_area.venue_type if media_area.provider == "foursquare" else None,
                client=client
            )
            return MediaArea(
                client=client,
                coordinates=MediaAreaCoordinates._parse(client, media_area.coordinates),
                type="venue",
                venue=venue
            )
        elif isinstance(media_area, raw.types.MediaAreaSuggestedReaction):
            reaction = types.Reaction._parse(client, media_area.reaction)
            return MediaArea(
                client=client,
                coordinates=MediaAreaCoordinates._parse(client, media_area.coordinates),
                type="reaction",
                reaction=reaction,
                is_dark=media_area.dark or None,
                is_flipped=media_area.flipped or None
            )
        elif isinstance(media_area, raw.types.MediaAreaChannelPost):
            return MediaArea(
                client=client,
                coordinates=MediaAreaCoordinates._parse(client, media_area.coordinates),
                type="channel_post",
                channel_id=media_area.channel_id,
                message_id=media_area.msg_id
            )
        elif isinstance(media_area, raw.types.MediaAreaUrl):
            return MediaArea(
                client=client,
                coordinates=MediaAreaCoordinates._parse(client, media_area.coordinates),
                type="url",
                url=media_area.url
            )
        elif isinstance(media_area, raw.types.MediaAreaWeather):
            return MediaArea(
                client=client,
                coordinates=MediaAreaCoordinates._parse(client, media_area.coordinates),
                type="weather"
            )
        elif isinstance(media_area, raw.types.MediaAreaStarGift):
            return MediaArea(
                client=client,
                coordinates=MediaAreaCoordinates._parse(client, media_area.coordinates),
                type="star_gift"
            )

        return None
