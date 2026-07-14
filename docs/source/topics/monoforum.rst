Monoforum
=========

Monoforum is a feature that allows channels to have a single-thread discussion area, similar to a simplified forum.

Checking Monoforum Status
-------------------------

Check if a channel has monoforum enabled:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        chat = await app.get_chat("channel_username")

        if chat.monoforum:
            print("This channel is a Monoforum")
            if chat.linked_monoforum_id:
                print(f"Linked Monoforum ID: {chat.linked_monoforum_id}")


    with app:
        app.loop.run_until_complete(main())

Handling Monoforum Updates
--------------------------

Handle monoforum read history updates:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    @app.on_raw_update()
    async def monoforum_update_handler(client, update, users, chats):
        from pyrogram.raw.types import UpdateReadMonoForumInbox, UpdateReadMonoForumOutbox

        if isinstance(update, UpdateReadMonoForumInbox):
            print(f"Monoforum inbox read up to {update.read_max_id}")

        if isinstance(update, UpdateReadMonoForumOutbox):
            print(f"Monoforum outbox read up to {update.read_max_id}")


    app.run()
