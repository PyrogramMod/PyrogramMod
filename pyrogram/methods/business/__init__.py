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

from .get_business_chat_links import GetBusinessChatLinks
from .create_business_chat_link import CreateBusinessChatLink
from .edit_business_chat_link import EditBusinessChatLink
from .delete_business_chat_link import DeleteBusinessChatLink
from .get_bot_business_connection import GetBotBusinessConnection
from .get_quick_replies import GetQuickReplies
from .get_quick_reply_messages import GetQuickReplyMessages
from .edit_quick_reply_shortcut import EditQuickReplyShortcut
from .delete_quick_reply_shortcut import DeleteQuickReplyShortcut
from .send_quick_reply_messages import SendQuickReplyMessages
from .check_quick_reply_shortcut import CheckQuickReplyShortcut
from .delete_quick_reply_messages import DeleteQuickReplyMessages

class Business(
    GetBusinessChatLinks,
    CreateBusinessChatLink,
    EditBusinessChatLink,
    DeleteBusinessChatLink,
    GetBotBusinessConnection,
    GetQuickReplies,
    GetQuickReplyMessages,
    EditQuickReplyShortcut,
    DeleteQuickReplyShortcut,
    SendQuickReplyMessages,
    CheckQuickReplyShortcut,
    DeleteQuickReplyMessages
):
    pass
