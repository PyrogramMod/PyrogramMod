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

from typing import Union, Optional

from pyrogram import raw
from pyrogram.scaffold import Scaffold


class CreateGroupCall(Scaffold):
    async def create_group_call(
            self,
            peer: Union[int, str],
            random_id: Union[str, int],
            rtmp_stream: Optional[bool],
            title: Optional[Union[str, int]],
            schedule_date: Optional[Union[int]]
    ):
        return await self.send(
            raw.functions.phone.CreateGroupCall(
                peer=await self.resolve_peer(peer),
                random_id=random_id,
                rtmp_stream=rtmp_stream,
                title=title,
                schedule_date=schedule_date,
            )
        )
