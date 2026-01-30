Suggested Posts
===============

Channels can have suggested posts that administrators can approve, edit, or refund.

Handling Suggested Posts
------------------------

Suggested posts appear in the :attr:`~pyrogram.types.Message.suggested_post` attribute:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    @app.on_message()
    async def suggested_post_handler(client, message):
        if message.suggested_post:
            print(f"New suggested post in {message.chat.title}")
            print(f"Suggested by: {message.suggested_post.user.first_name}")

            if message.suggested_post.stars:
                print(f"Price: {message.suggested_post.stars.amount} Stars")


    app.run()

Service Messages
----------------

Handle suggested post lifecycle events:

.. code-block:: python

    from pyrogram import Client, enums

    app = Client("my_account")


    @app.on_message()
    async def suggested_post_service_handler(client, message):
        if message.service == enums.MessageServiceType.SUGGESTED_POST_APPROVAL:
            print("A suggested post was approved!")

        if message.service == enums.MessageServiceType.SUGGESTED_POST_SUCCESS:
            print("A suggested post was successfully published!")

        if message.service == enums.MessageServiceType.SUGGESTED_POST_REFUND:
            print("A suggested post was refunded.")


    app.run()
