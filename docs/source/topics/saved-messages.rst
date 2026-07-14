Saved Messages Improvements
===========================

Telegram has enhanced Saved Messages with peer-based organization and reaction tags.

Organizing by Peer
------------------

Retrieve Saved Messages dialogs organized by the original peer:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        saved_dialogs = await app.get_saved_dialogs()

        for dialog in saved_dialogs.dialogs:
            print(f"Saved from: {dialog.peer.title or dialog.peer.first_name}")
            print(f"Last message: {dialog.top_message.text}")


    with app:
        app.loop.run_until_complete(main())

Reaction Tags
-------------

Manage reaction tags used to categorize your saved messages:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        tags = await app.get_saved_reaction_tags()

        for tag in tags:
            print(f"Tag: {tag.reaction} (used in {tag.count} messages)")
            if tag.title:
                print(f"Custom name: {tag.title}")

        # Set a custom name for a reaction tag
        await app.update_saved_reaction_tag("❤️", title="Favorites")


    with app:
        app.loop.run_until_complete(main())

Pinning Saved Dialogs
---------------------

Pin important peer-folders in your Saved Messages:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        # Pin a user folder in saved messages
        await app.pin_saved_dialog("username")

        # Get only pinned folders
        pinned = await app.get_pinned_saved_dialogs()


    with app:
        app.loop.run_until_complete(main())
