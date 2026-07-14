Boosts and Giveaways
====================

Telegram channels support boosts and giveaways to grow and engage with audiences.

Channel Boosts
--------------

Get boost status for a channel:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        boost_status = await app.get_boost_status("channel_username")

        print(f"Total boosts: {boost_status.level}")
        print(f"Current level: {boost_status.current_level_boosts}")
        print(f"Boosts to next level: {boost_status.boosts}")


    with app:
        app.loop.run_until_complete(main())

Applying Boosts
---------------

Apply a boost to a channel:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        await app.apply_boost("channel_username")
        print("Boost applied successfully!")


    with app:
        app.loop.run_until_complete(main())

Getting Boosts List
-------------------

Retrieve the list of boosts for a channel:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    async def main():
        boosts = await app.get_boosts_list("channel_username")

        for boost in boosts:
            print(f"Boost from: {boost.user_id}")
            print(f"Date: {boost.date}")


    with app:
        app.loop.run_until_complete(main())

Handling Boost Updates
-----------------------

Handle boost updates with a handler:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.handlers import ChatBoostHandler

    app = Client("my_bot_token")


    async def boost_handler(client, boost):
        print(f"New boost in {boost.chat.title}")
        print(f"Boost count: {boost.boost.boosts}")


    app.add_handler(ChatBoostHandler(boost_handler))
    app.run()

Giveaway Messages
-----------------

Handle giveaway-related messages:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    @app.on_message()
    async def giveaway_handler(client, message):
        if message.giveaway:
            print(f"Giveaway for {message.giveaway.quantity} prizes")
            print(f"Ends: {message.giveaway.until_date}")
            print(f"Channels: {[c.title for c in message.giveaway.channels]}")

        if message.giveaway_results:
            print(f"Winners: {message.giveaway_results.winners_count}")
            print(f"Unclaimed: {message.giveaway_results.unclaimed_count}")


    app.run()
