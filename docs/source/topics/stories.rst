Stories
=======

Pyrogram supports Telegram Stories, allowing you to create, view, and interact with stories.

Receiving Stories
-----------------

You can handle story updates using the :class:`~pyrogram.handlers.StoryHandler`:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    @app.on_story()
    async def story_handler(client, story):
        print(f"New story from {story.chat.title}: {story.caption}")


    app.run()

Sending Stories
---------------

Send a photo or video story:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        await app.send_story(
            "me",
            "photo.jpg",
            caption="Check out my new story!"
        )


    with app:
        app.loop.run_until_complete(main())

Getting Stories
---------------

Retrieve stories from a chat:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        stories = await app.get_stories("username")

        for story in stories:
            print(f"Story ID: {story.id}")
            print(f"Caption: {story.caption}")


    with app:
        app.loop.run_until_complete(main())

Deleting Stories
----------------

Delete your own stories:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        await app.delete_stories("me", [story_id1, story_id2])


    with app:
        app.loop.run_until_complete(main())

Story Privacy
-------------

Control who can see your stories:

.. code-block:: python

    from pyrogram import Client, enums

    app = Client("my_account")


    async def main():
        await app.send_story(
            "me",
            "photo.jpg",
            privacy=enums.StoryPrivacyType.CONTACTS
        )


    with app:
        app.loop.run_until_complete(main())
