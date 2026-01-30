styled_keyboards
================

This example shows how to use the new KeyboardButtonStyle to create styled keyboard buttons with custom colors and icons.

Available since Layer 224, keyboard buttons can now have custom styles including background colors (primary, danger, success) and custom emoji icons.

.. code-block:: python

    from pyrogram import Client
    from pyrogram.types import (
        ReplyKeyboardMarkup,
        KeyboardButton,
        KeyboardButtonStyle
    )

    # Create a client using your bot token
    app = Client("my_bot", bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")


    async def main():
        async with app:
            # Example 1: Button with primary (blue) background
            await app.send_message(
                "me",  # Edit this
                "Styled keyboard with primary button",
                reply_markup=ReplyKeyboardMarkup(
                    [[
                        KeyboardButton(
                            text="Primary Action",
                            style=KeyboardButtonStyle(bg_primary=True)
                        )
                    ]],
                    resize_keyboard=True
                )
            )

            # Example 2: Button with danger (red) background
            await app.send_message(
                "me",  # Edit this
                "Styled keyboard with danger button",
                reply_markup=ReplyKeyboardMarkup(
                    [[
                        KeyboardButton(
                            text="Delete All",
                            style=KeyboardButtonStyle(bg_danger=True)
                        )
                    ]],
                    resize_keyboard=True
                )
            )

            # Example 3: Button with success (green) background
            await app.send_message(
                "me",  # Edit this
                "Styled keyboard with success button",
                reply_markup=ReplyKeyboardMarkup(
                    [[
                        KeyboardButton(
                            text="Confirm",
                            style=KeyboardButtonStyle(bg_success=True)
                        )
                    ]],
                    resize_keyboard=True
                )
            )

            # Example 4: Button with custom emoji icon
            await app.send_message(
                "me",  # Edit this
                "Styled keyboard with icon",
                reply_markup=ReplyKeyboardMarkup(
                    [[
                        KeyboardButton(
                            text="Settings",
                            style=KeyboardButtonStyle(
                                icon=5368324170671202286  # Custom emoji ID
                            )
                        )
                    ]],
                    resize_keyboard=True
                )
            )

            # Example 5: Mixed styles in one keyboard
            await app.send_message(
                "me",  # Edit this
                "Choose an action:",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        [
                            KeyboardButton(
                                text="Save",
                                style=KeyboardButtonStyle(bg_success=True)
                            ),
                            KeyboardButton(
                                text="Cancel",
                                style=KeyboardButtonStyle(bg_danger=True)
                            )
                        ],
                        [
                            KeyboardButton(
                                text="More Options",
                                style=KeyboardButtonStyle(bg_primary=True)
                            )
                        ]
                    ],
                    resize_keyboard=True
                )
            )


    app.run(main())
