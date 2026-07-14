from .delete_ephemeral_message import DeleteEphemeralMessage
from .get_ephemeral_callback_answer import GetEphemeralCallbackAnswer
from .report_ephemeral_message import ReportEphemeralMessage
from .send_ephemeral_message import SendEphemeralMessage
from .edit_ephemeral_message_text import EditEphemeralMessageText
from .edit_ephemeral_message_caption import EditEphemeralMessageCaption
from .edit_ephemeral_message_media import EditEphemeralMessageMedia
from .edit_ephemeral_message_reply_markup import EditEphemeralMessageReplyMarkup


class Ephemeral(
    DeleteEphemeralMessage,
    GetEphemeralCallbackAnswer,
    ReportEphemeralMessage,
    SendEphemeralMessage,
    EditEphemeralMessageText,
    EditEphemeralMessageCaption,
    EditEphemeralMessageMedia,
    EditEphemeralMessageReplyMarkup,
):
    pass
