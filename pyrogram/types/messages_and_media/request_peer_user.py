from pyrogram import raw
from pyrogram.raw.base import InputPeer
from pyrogram.types import Object


class RequestPeerUser(Object):
    def __init__(
            self,
            *,
            button_id: str,
            premium: int,
    ):
        super().__init__()

        self.button_id = button_id
        self.peer = peer

    @staticmethod
    def _parse(action: raw.types.RequestPeerTypeBroadcast):
            return RequestPeerUser(
                button_id=action.,
                chat_id=action.peer
            )
