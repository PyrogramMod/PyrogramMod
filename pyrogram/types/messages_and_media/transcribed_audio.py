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

from typing import Optional

import pyrogram
from pyrogram import raw
from ..object import Object


class TranscribedAudio(Object):
    """Transcription of a voice or audio message.

    Parameters:
        id (``int``):
            Identifier of the transcription. Updates with the final text arrive as
            :obj:`~pyrogram.types.TranscriptionUpdate` while *is_pending* is True.

        text (``str``):
            Transcribed text, possibly partial.

        is_pending (``bool``):
            True, if the transcription is not final yet.

        trial_remains_num (``int``, *optional*):
            Free transcriptions left in the trial.

        trial_remains_until_date (``int``, *optional*):
            Unix time the trial period ends.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        text: str,
        is_pending: bool = False,
        trial_remains_num: Optional[int] = None,
        trial_remains_until_date: Optional[int] = None
    ):
        super().__init__(client)

        self.id = id
        self.text = text
        self.is_pending = is_pending
        self.trial_remains_num = trial_remains_num
        self.trial_remains_until_date = trial_remains_until_date

    @staticmethod
    def _parse(client, r: "raw.types.messages.TranscribedAudio") -> "TranscribedAudio":
        return TranscribedAudio(
            id=r.transcription_id,
            text=r.text,
            is_pending=bool(r.pending),
            trial_remains_num=r.trial_remains_num,
            trial_remains_until_date=r.trial_remains_until_date,
            client=client
        )
