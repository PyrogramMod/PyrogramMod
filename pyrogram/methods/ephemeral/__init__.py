from .delete_ephemeral_message import DeleteEphemeralMessage
from .get_ephemeral_callback_answer import GetEphemeralCallbackAnswer
from .report_ephemeral_message import ReportEphemeralMessage
from .send_ephemeral_message import SendEphemeralMessage


class Ephemeral(
    DeleteEphemeralMessage,
    GetEphemeralCallbackAnswer,
    ReportEphemeralMessage,
    SendEphemeralMessage,
):
    pass
