Privacy Settings
================

Telegram has introduced new privacy keys and values to give users more control over their information.

New Privacy Keys
----------------

You can now manage privacy for the following categories:

- **About**: Control who can see your bio/about text.
- **Birthday**: Control who can see your birthday.
- **Star Gifts**: Control who can see your received star gifts on your profile.
- **Paid Messages**: Control who can send you paid messages.
- **Saved Music**: Control who can see your saved music.

.. code-block:: python

    from pyrogram import Client, enums

    app = Client("my_account")

    async def main():
        # Get privacy for birthday
        privacy = await app.get_privacy(enums.PrivacyKeyType.BIRTHDAY)
        print(f"Birthday privacy: {privacy}")

    app.run(main())

New Privacy Rules
-----------------

New values are available to define more granular permissions:

- **Allow Close Friends**: Only users in your close friends list.
- **Allow Premium**: Only Telegram Premium users.
- **Allow Bots / Disallow Bots**: Specifically allow or disallow all bots.

.. code-block:: python

    from pyrogram import Client, enums, raw

    async def main():
        # Allow only premium users to send you messages
        await app.set_privacy(
            enums.PrivacyKeyType.CHAT_INVITE,
            [raw.types.InputPrivacyValueAllowPremium()]
        )
