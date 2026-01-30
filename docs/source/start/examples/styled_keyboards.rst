styled_keyboards
================

This example shows how to use the new KeyboardButtonStyle to create styled keyboard buttons with custom colors and icons.

Available since Layer 224, keyboard buttons can now have custom styles including background colors (primary, danger, success) and custom emoji icons. This works for both ReplyKeyboardMarkup (regular keyboards) and InlineKeyboardMarkup (inline buttons).

Reply Keyboard Examples
-----------------------

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

Inline Keyboard Examples
------------------------

.. code-block:: python

    from pyrogram import Client
    from pyrogram.types import (
        InlineKeyboardMarkup,
        InlineKeyboardButton,
        KeyboardButtonStyle,
        WebAppInfo,
        LoginUrl
    )

    # Create a client using your bot token
    app = Client("my_bot", bot_token="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")


    async def main():
        async with app:
            # Example 1: Callback button with primary (blue) background
            await app.send_message(
                "me",  # Edit this
                "Callback button example:",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="Click Me",
                            callback_data="clicked",
                            style=KeyboardButtonStyle(bg_primary=True)
                        )
                    ]]
                )
            )

            # Example 2: URL button with danger (red) style
            await app.send_message(
                "me",  # Edit this
                "URL button example:",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="Open Website",
                            url="https://example.com",
                            style=KeyboardButtonStyle(bg_danger=True)
                        )
                    ]]
                )
            )

            # Example 3: Switch inline query button with success (green) style
            await app.send_message(
                "me",  # Edit this
                "Inline query buttons:",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Search in other chat",
                                switch_inline_query="search query",
                                style=KeyboardButtonStyle(bg_primary=True)
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="Search here",
                                switch_inline_query_current_chat="search query",
                                style=KeyboardButtonStyle(bg_success=True)
                            )
                        ]
                    ]
                )
            )

            # Example 4: User profile button with custom emoji icon
            await app.send_message(
                "me",  # Edit this
                "User profile button:",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="View Profile",
                            user_id=123456789,  # Replace with actual user ID
                            style=KeyboardButtonStyle(
                                icon=5368324170671202286  # Custom emoji ID
                            )
                        )
                    ]]
                )
            )

            # Example 5: WebApp button with primary style
            await app.send_message(
                "me",  # Edit this
                "WebApp button:",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="Open WebApp",
                            web_app=WebAppInfo(url="https://example.com/webapp"),
                            style=KeyboardButtonStyle(bg_primary=True)
                        )
                    ]]
                )
            )

            # Example 6: Login URL button with style
            await app.send_message(
                "me",  # Edit this
                "Login button:",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="Login with Telegram",
                            login_url=LoginUrl(
                                url="https://example.com/login",
                                forward_text="Login to Example",
                                request_write_access=True
                            ),
                            style=KeyboardButtonStyle(bg_success=True)
                        )
                    ]]
                )
            )

            # Example 7: All button types in one keyboard
            await app.send_message(
                "me",  # Edit this
                "Complete keyboard with all styled button types:",
                reply_markup=InlineKeyboardMarkup(
                    [
                        # Row 1: Callback buttons
                        [
                            InlineKeyboardButton(
                                text="✅ Confirm",
                                callback_data="confirm",
                                style=KeyboardButtonStyle(bg_success=True)
                            ),
                            InlineKeyboardButton(
                                text="❌ Cancel",
                                callback_data="cancel",
                                style=KeyboardButtonStyle(bg_danger=True)
                            )
                        ],
                        # Row 2: URL button
                        [
                            InlineKeyboardButton(
                                text="🌐 Visit Website",
                                url="https://example.com",
                                style=KeyboardButtonStyle(bg_primary=True)
                            )
                        ],
                        # Row 3: Inline query buttons
                        [
                            InlineKeyboardButton(
                                text="🔍 Search",
                                switch_inline_query_current_chat="",
                                style=KeyboardButtonStyle(
                                    icon=5368324170671202286  # Search emoji
                                )
                            )
                        ]
                    ]
                )
            )


    app.run(main())
