Business Features
=================

Telegram Business accounts offer special features for business automation.

Handling Business Messages
---------------------------

Receive and handle messages from business chats:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_bot_token")


    @app.on_message()
    async def business_message_handler(client, message):
        print(f"Business message: {message.text}")


    app.run()

Business Connections
--------------------

Handle business connection updates:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.handlers import BusinessConnectionHandler

    app = Client("my_bot_token")


    async def connection_handler(client, connection):
        print(f"Connected to business: {connection.user.username}")
        print(f"Connection ID: {connection.id}")


    app.add_handler(BusinessConnectionHandler(connection_handler))
    app.run()

Quick Replies
-------------

Business accounts can use quick reply shortcuts. Messages with quick replies have the
:attr:`~pyrogram.types.Message.quick_reply_shortcut_id` attribute set.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    @app.on_message()
    async def handle_quick_reply(client, message):
        if message.quick_reply_shortcut_id:
            print(f"Sent using quick reply: {message.quick_reply_shortcut_id}")


    app.run()

Business Information
--------------------

Access business account information including work hours, location, and greeting messages:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        chat = await app.get_chat("business_username")

        if chat.business_info:
            print(f"Work hours: {chat.business_info.business_hours}")
            print(f"Location: {chat.business_info.location}")
            print(f"Intro: {chat.business_info.intro}")


    with app:
        app.loop.run_until_complete(main())
