from pyrogram.types import Object


class RequestPeerChat(Object):
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
            return RequestPeerChat(
                button_id=action.,
                chat_id=action.peer
            )
