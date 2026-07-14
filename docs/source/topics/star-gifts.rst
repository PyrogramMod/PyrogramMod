Star Gifts
==========

Telegram Star Gifts allow users to send unique stickers and collectibles using Telegram Stars.

Handling Star Gifts
-------------------

Receive and parse star gift service messages:

.. code-block:: python

    from pyrogram import Client, enums

    app = Client("my_account")


    @app.on_message()
    async def star_gift_handler(client, message):
        if message.service == enums.MessageServiceType.STAR_GIFT:
            gift = message.star_gift
            print(f"Received gift: {gift.title}")
            print(f"Price: {gift.stars} stars")
            print(f"Convert value: {gift.convert_stars} stars")

        if message.service == enums.MessageServiceType.STAR_GIFT_UNIQUE:
            unique_gift = message.star_gift_unique
            print(f"Received unique gift: {unique_gift.title} #{unique_gift.num}")
            print(f"Slug: {unique_gift.slug}")


    app.run()

Getting Available Gifts
-----------------------

Get a list of gifts available for purchase:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        gifts = await app.get_star_gifts()

        for gift in gifts:
            print(f"Gift: {gift.title} ({gift.stars} Stars)")
            if gift.limited:
                print(f"Limited: {gift.availability_remains}/{gift.availability_total}")


    with app:
        app.loop.run_until_complete(main())

Managing Saved Gifts
--------------------

Retrieve and manage gifts saved on your profile:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        # Get your own saved gifts
        saved_gifts = await app.get_saved_star_gifts("me")

        for gift in saved_gifts:
            print(f"Saved unique gift: {gift.title} #{gift.num}")


    with app:
        app.loop.run_until_complete(main())
