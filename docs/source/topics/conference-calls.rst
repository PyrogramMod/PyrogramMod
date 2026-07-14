Conference Calls
================

Telegram Group Calls have been enhanced with conference features.

Checking Conference Support
---------------------------

Check if a group call supports conference mode:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        chat = await app.get_chat("group_username")
        call = chat.call

        if call and call.is_conference:
            print("This is a conference call")
            print(f"Title: {call.title}")


    with app:
        app.loop.run_until_complete(main())

Handling Call Events
--------------------

Handle service messages related to conference calls:

.. code-block:: python

    from pyrogram import Client, enums

    app = Client("my_account")


    @app.on_message()
    async def call_handler(client, message):
        if message.service == enums.MessageServiceType.CONFERENCE_CALL:
            print(f"Conference call action in {message.chat.title}")


    app.run()
