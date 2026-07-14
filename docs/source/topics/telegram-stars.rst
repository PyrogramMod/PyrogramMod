Telegram Stars
==============

Telegram Stars is a virtual currency system for paid content and monetization.

Checking Stars Balance
----------------------

Get your current Stars balance:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        status = await app.get_stars_status()
        print(f"Balance: {status.balance.amount} stars")


    with app:
        app.loop.run_until_complete(main())

Getting Transactions
--------------------

View Stars transaction history:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        transactions = await app.get_stars_transactions()

        for transaction in transactions:
            print(f"Amount: {transaction.stars.amount}")
            print(f"Date: {transaction.date}")


    with app:
        app.loop.run_until_complete(main())

Handling Paid Media
-------------------

Messages with paid media can be accessed through the :attr:`~pyrogram.types.Message.paid_media` attribute:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    @app.on_message()
    async def handle_paid_media(client, message):
        if message.paid_media:
            print(f"Paid media costs {message.paid_media.stars_amount} stars")

            for media in message.paid_media.extended_media:
                if isinstance(media, dict) and media.get("type") == "preview":
                    print("Preview only - purchase to see full media")
                else:
                    print(f"Media: {media}")


    app.run()

Star Gifts
----------

Handle star gift messages:

.. code-block:: python

    from pyrogram import Client, enums

    app = Client("my_account")


    @app.on_message()
    async def handle_star_gift(client, message):
        if message.service == enums.MessageServiceType.STAR_GIFT:
            print(f"Received a star gift in chat {message.chat.id}")


    app.run()
