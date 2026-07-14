star_gifts
==========

This example shows how to handle Star Gift service messages.

Star Gifts are a Telegram feature that allows users to send gifts to each other. When a gift is received,
a service message is sent with the gift details. This example demonstrates how to detect and handle these messages.

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.enums import MessageServiceType

    app = Client("my_account")


    @app.on_message(filters.service)
    async def handle_service_messages(client, message):
        """Handle service messages including star gifts."""

        # Check if this is a star gift message
        if message.service == MessageServiceType.STAR_GIFT:
            print(f"Received a Star Gift!")
            print(f"Message ID: {message.id}")
            print(f"From: {message.from_user.first_name if message.from_user else 'Anonymous'}")
            print(f"Date: {message.date}")

            # You can access the raw action for more details
            # The raw action contains: gift, name_hidden, saved, converted, etc.

        elif message.service == MessageServiceType.STAR_GIFT_UNIQUE:
            print(f"Received a Unique/Collectible Star Gift!")
            print(f"Message ID: {message.id}")
            print(f"This is a special collectible gift that can be traded as NFT")

        elif message.service == MessageServiceType.NEW_CREATOR_PENDING:
            print(f"Creator transfer is pending!")
            print(f"A new creator has been nominated for this channel/group")

        elif message.service == MessageServiceType.CHANGE_CREATOR:
            print(f"Creator has been changed!")
            print(f"The ownership of this channel/group has been transferred")


    @app.on_message(filters.service)
    async def log_all_service_types(client, message):
        """Log all service message types for debugging."""
        if message.service:
            print(f"Service message type: {message.service}")


    app.run()


Using StarGift and StarGiftUnique Types
---------------------------------------

The high-level ``StarGift`` and ``StarGiftUnique`` types provide easy access to gift properties:

.. code-block:: python

    from pyrogram.types import StarGift, StarGiftUnique

    # StarGift properties:
    # - id: Unique identifier of the gift
    # - sticker: Sticker representing the gift
    # - stars: Price in Telegram Stars
    # - convert_stars: Stars the receiver can convert to
    # - limited: Whether it's a limited-supply gift
    # - sold_out: Whether the gift sold out
    # - birthday: Whether it's a birthday-themed gift
    # - can_upgrade: Whether it can be upgraded to collectible
    # - availability_remains: Remaining gifts (for limited)
    # - availability_total: Total supply (for limited)

    # StarGiftUnique properties (collectible gifts):
    # - id: Unique identifier
    # - gift_id: Base gift type ID
    # - title: Collectible title
    # - slug: For creating deep links
    # - num: Unique number among collectibles of same type
    # - burned: Whether the gift was burned
    # - crafted: Whether it was crafted
    # - owner_id: User ID of owner
    # - owner_address: TON blockchain address
    # - gift_address: NFT address on blockchain


Filtering Star Gift Messages
----------------------------

You can create a custom filter for star gift messages:

.. code-block:: python

    from pyrogram import Client, filters
    from pyrogram.enums import MessageServiceType

    # Custom filter for star gifts
    star_gift_filter = filters.create(
        lambda _, __, m: m.service in (
            MessageServiceType.STAR_GIFT,
            MessageServiceType.STAR_GIFT_UNIQUE
        )
    )

    app = Client("my_account")


    @app.on_message(star_gift_filter)
    async def on_star_gift(client, message):
        """Handle only star gift messages."""
        if message.service == MessageServiceType.STAR_GIFT:
            await message.reply("Thank you for the star gift! ⭐")
        else:
            await message.reply("Wow, a unique collectible gift! 🎁")


    app.run()
