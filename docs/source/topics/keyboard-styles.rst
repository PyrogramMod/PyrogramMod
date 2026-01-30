Keyboard Button Styles
======================

Pyrogram now supports styled inline and reply keyboard buttons.

Button Styles
-------------

Buttons can have different visual styles using the :class:`~pyrogram.enums.KeyboardButtonStyle` enum:

- **PRIMARY**: Default blue style.
- **DANGER**: Red style for destructive actions.
- **SUCCESS**: Green style for positive actions.

.. code-block:: python

    from pyrogram import Client, types, enums

    app = Client("my_account")

    async def main():
        await app.send_message(
            "chat_id",
            "Choose an action:",
            reply_markup=types.InlineKeyboardMarkup([
                [
                    types.InlineKeyboardButton(
                        "Delete Record",
                        callback_data="delete",
                        style=enums.KeyboardButtonStyle.DANGER
                    ),
                    types.InlineKeyboardButton(
                        "Save Changes",
                        callback_data="save",
                        style=enums.KeyboardButtonStyle.SUCCESS
                    )
                ]
            ])
        )

    app.run(main())

Button Icons
------------

You can also attach custom icons to buttons:

.. code-block:: python

    from pyrogram import Client, types

    async def main():
        await app.send_message(
            "chat_id",
            "Settings:",
            reply_markup=types.ReplyKeyboardMarkup([
                [
                    types.KeyboardButton(
                        "Notifications",
                        icon=123456789  # Custom Emoji ID
                    )
                ]
            ])
        )
