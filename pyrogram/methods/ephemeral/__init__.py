from .delete_ephemeral_message import DeleteEphemeralMessage
from .get_ephemeral_callback_answer import GetEphemeralCallbackAnswer
from .report_ephemeral_message import ReportEphemeralMessage
from .send_ephemeral_message import SendEphemeralMessage
from .get_welcome_messages import GetWelcomeMessages
from .delete_welcome_message import DeleteWelcomeMessage
from .delete_all_welcome_messages import DeleteAllWelcomeMessages
from .forward_welcome_message import ForwardWelcomeMessage
from .edit_ephemeral_message import EditEphemeralMessage


class Ephemeral(
    DeleteEphemeralMessage,
    GetEphemeralCallbackAnswer,
    ReportEphemeralMessage,
    SendEphemeralMessage,
    GetWelcomeMessages,
    DeleteWelcomeMessage,
    DeleteAllWelcomeMessages,
    ForwardWelcomeMessage,
    EditEphemeralMessage,
):
    pass
