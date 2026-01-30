Miscellaneous Updates
=====================

This section covers various smaller features and improvements introduced in recent layers.

Birthday Feature
----------------

Users can now set and share their birthdays.

.. code-block:: python

    from pyrogram import Client

    async def main():
        user = await app.get_chat("me")
        if user.birthday:
            print(f"Birthday: {user.birthday.day}/{user.birthday.month}/{user.birthday.year}")

Paid Reactions
--------------

Support for Telegram Stars-based reactions:

.. code-block:: python

    from pyrogram import Client

    async def main():
        # Send a paid reaction (1 Star)
        await app.send_paid_reaction("chat_id", message_id=123, count=1)

Audio Transcription
-------------------

Handle audio transcription updates:

.. code-block:: python

    from pyrogram import Client

    @app.on_raw_update()
    async def handle_transcription(client, update, users, chats):
        from pyrogram.raw.types import UpdateTranscribeAudio

        if isinstance(update, UpdateTranscribeAudio):
            print(f"Transcription: {update.text}")

Emoji Game Results
------------------

Dice messages now include the specific game outcome:

.. code-block:: python

    @app.on_message()
    async def dice_handler(client, message):
        if message.dice:
            print(f"Value: {message.dice.value}")
            if message.dice.game_outcome:
                print(f"Outcome: {message.dice.game_outcome}")
