Streaming replies
=================
Telegram bots can now keep independent threaded conversations so AI assistants handle multiple topics in parallel. While an answer is being generated you can stream intermediate text, letting Telegram display the native “Thinking…” chip exactly like the official AI bot experience.

See the official announcement_ for a quick overview. You can pass either a single string or a list of strings to ``send_streaming_text``—each string becomes one chunk in the typing stream.

.. _announcement: https://telegram.org/blog/comments-in-video-chats-threads-for-bots/it?setln=en#threads-and-streaming-responses-for-ai-bots

.. code-block:: python
   :caption: streaming_text.py

    from pyrogram import Client, filters

    app = Client("streaming-example")

    @app.on_message(filters.command("ai"))
    async def stream_reply(client, message):
        streaming_chunks = [
            "Hello! Let me think…",
            "OK, I see what you need…",
            "Working out the details…",
            "Here comes the final advice…"
        ]

        await client.send_streaming_text(
            chat_id=message.chat.id,
            streaming_text=streaming_chunks,
            message_thread_id=message.message_thread_id
        )
        # Or, for a single status update:
        # await client.send_streaming_text(chat_id=message.chat.id, streaming_text="Hello! Let me think…")

    app.run()
