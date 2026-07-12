PEER_ID_INVALID error
=====================

This error could mean several things:

- The chat id you tried to use is simply wrong, check it again.
- The chat id refers to a group or channel you are not a member of.
- The chat id argument you passed is in form of a string; you have to convert it into an integer with ``int(chat_id)``.
- The chat id refers to a user or chat your current session hasn't met yet.

About the last point: in order for you to meet a user and thus communicate with them, you should ask yourself how to
contact people using official apps. The answer is the same for Pyrogram too and involves normal usages such as searching
for usernames, meeting them in a common group, having their phone contacts saved, getting a message mentioning them
or obtaining the dialogs list.

Community IDs
-------------

Communities (introduced in layer 228) use a **different ID space** from regular channels and supergroups.
Their IDs are raw integers (e.g. ``1095605184288``) and are **not** prefixed with ``-100``.
You can obtain a community ID from:

- The ``linked_community_id`` field on :obj:`~pyrogram.types.Chat` — populated when a channel belongs to a community.
- :meth:`~pyrogram.Client.get_joined_communities` — returns all communities you are a member of, each with its raw ID and ``access_hash``.

Community IDs cannot be passed directly to methods that call ``resolve_peer`` internally (such as
:meth:`~pyrogram.Client.get_chat`). Methods in the ``communities.*`` namespace (e.g.
:meth:`~pyrogram.Client.add_chat_to_community`) handle this automatically.