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

import math
from asyncio import Lock, sleep
from time import monotonic


class DownloadRequestPacer:
    """Gradual request pacing adapted from TGA-Dec's DownloadRequestPacer."""

    def __init__(self):
        self.interval_ms = 50.0
        self.next_request_at = 0.0
        self.cooldown_until = 0.0
        self.lock = Lock()

    def defer(self, seconds):
        now = monotonic() * 1000
        new_cooldown = now >= self.cooldown_until
        deadline = now + seconds * 1000
        self.cooldown_until = max(self.cooldown_until, deadline)
        # wait() holds the lock while sleeping, so register the delay immediately.
        self.next_request_at = max(self.next_request_at, deadline)
        return new_cooldown

    async def wait(self):
        async with self.lock:
            now = monotonic() * 1000
            while now < self.next_request_at:
                await sleep((self.next_request_at - now) / 1000)
                now = monotonic() * 1000
            self.next_request_at = now + math.ceil(self.interval_ms)
            self.interval_ms = max(3.0, self.interval_ms * 0.8)
