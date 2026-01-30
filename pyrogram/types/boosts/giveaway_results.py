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
from typing import Optional, List

import pyrogram
from pyrogram import raw, types, utils
from ..object import Object


class GiveawayResults(Object):
    """Represents the results of a giveaway.

    Parameters:
        chat (:obj:`~pyrogram.types.Chat`):
            The chat that created the giveaway.

        giveaway_message_id (``int``):
            The message ID of the giveaway.

        winners_count (``int``):
            Total number of winners.

        unclaimed_count (``int``):
            Number of unclaimed prizes.

        winners (List of :obj:`~pyrogram.types.User`):
            List of winner users.

        launch_message_id (``int``, *optional*):
            Message ID of the launch message.

        additional_chats (List of :obj:`~pyrogram.types.Chat`, *optional*):
            Additional channels that were part of the giveaway.

        date (``datetime``, *optional*):
            When the giveaway started.

        until_date (``datetime``, *optional*):
            When the giveaway ended.

        months (``int``, *optional*):
            Number of months of Premium subscription as prize.

        stars (``int``, *optional*):
            Amount of Telegram Stars as prize.

        prize_description (``str``, *optional*):
            Description of additional prizes.

        is_only_new_subscribers (``bool``, *optional*):
            Whether the giveaway was only for new subscribers.

        is_refunded (``bool``, *optional*):
            Whether the giveaway was refunded.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        chat: "types.Chat" = None,
        giveaway_message_id: int = None,
        winners_count: int = None,
        unclaimed_count: int = None,
        winners: List["types.User"] = None,
        launch_message_id: int = None,
        additional_chats: List["types.Chat"] = None,
        date: datetime = None,
        until_date: datetime = None,
        months: int = None,
        stars: int = None,
        prize_description: str = None,
        is_only_new_subscribers: bool = None,
        is_refunded: bool = None
    ):
        super().__init__(client)

        self.chat = chat
        self.giveaway_message_id = giveaway_message_id
        self.winners_count = winners_count
        self.unclaimed_count = unclaimed_count
        self.winners = winners
        self.launch_message_id = launch_message_id
        self.additional_chats = additional_chats
        self.date = date
        self.until_date = until_date
        self.months = months
        self.stars = stars
        self.prize_description = prize_description
        self.is_only_new_subscribers = is_only_new_subscribers
        self.is_refunded = is_refunded

    @staticmethod
    def _parse(
        client: "pyrogram.Client",
        results: "raw.types.MessageMediaGiveawayResults",
        users: dict,
        chats: dict
    ) -> "GiveawayResults":
        # Parse the main chat
        chat = None
        if results.channel_id:
            peer = chats.get(results.channel_id)
            if peer:
                chat = types.Chat._parse_channel_chat(client, peer)

        # Parse winners
        winners = []
        if results.winners:
            for user_id in results.winners:
                if user_id in users:
                    winners.append(types.User._parse(client, users[user_id]))

        # Parse additional chats
        additional_chats = []
        if hasattr(results, 'additional_peers') and results.additional_peers:
            for peer_id in results.additional_peers:
                if peer_id in chats:
                    additional_chats.append(
                        types.Chat._parse_channel_chat(client, chats[peer_id])
                    )

        return GiveawayResults(
            client=client,
            chat=chat,
            giveaway_message_id=results.launch_msg_id,
            winners_count=results.winners_count,
            unclaimed_count=results.unclaimed_count,
            winners=types.List(winners) if winners else None,
            launch_message_id=results.launch_msg_id,
            additional_chats=types.List(additional_chats) if additional_chats else None,
            date=utils.timestamp_to_datetime(results.start_date) if hasattr(results, 'start_date') and results.start_date else None,
            until_date=utils.timestamp_to_datetime(results.until_date) if hasattr(results, 'until_date') and results.until_date else None,
            months=results.months if hasattr(results, 'months') else None,
            stars=results.stars if hasattr(results, 'stars') else None,
            prize_description=results.prize_description if hasattr(results, 'prize_description') else None,
            is_only_new_subscribers=results.only_new_subscribers if hasattr(results, 'only_new_subscribers') else None,
            is_refunded=results.refunded if hasattr(results, 'refunded') else None
        )
