from .add_chat_to_community import AddChatToCommunity
from .approve_all_community_peer_links import ApproveAllCommunityPeerLinks
from .approve_community_peer_link import ApproveCommunityPeerLink
from .ban_community_participant import BanCommunityParticipant
from .create_community import CreateCommunity
from .get_community_participant_chats import GetCommunityParticipantChats
from .get_community_peer_link_requests import GetCommunityPeerLinkRequests
from .get_joined_communities import GetJoinedCommunities
from .toggle_community_collapsed import ToggleCommunityCollapsed
from .toggle_community_peer_link import ToggleCommunityPeerLink


class Communities(
    AddChatToCommunity,
    ApproveAllCommunityPeerLinks,
    ApproveCommunityPeerLink,
    BanCommunityParticipant,
    CreateCommunity,
    GetCommunityParticipantChats,
    GetCommunityPeerLinkRequests,
    GetJoinedCommunities,
    ToggleCommunityCollapsed,
    ToggleCommunityPeerLink,
):
    pass
