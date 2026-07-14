To-Do Lists
===========

Telegram supports collaborative to-do lists in chats.

Handling To-Do Messages
------------------------

Receive and display to-do lists in messages:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    @app.on_message()
    async def todo_handler(client, message):
        if message.todo:
            print(f"To-Do List: {message.todo.title}")
            print(f"Total items: {message.todo.total_count}")

            for item in message.todo.items:
                status = "✓" if item.is_checked else "○"
                print(f"{status} {item.text}")

            if message.todo.completions:
                print(f"Completed: {message.todo.completed_count}")


    app.run()

Sending To-Do Lists
-------------------

Send a to-do list to a chat:

.. code-block:: python

    from pyrogram import Client
    from pyrogram.types import InputMediaTodo

    app = Client("my_account")


    async def main():
        await app.send_media_group(
            "chat_id",
            media=[
                InputMediaTodo(
                    title="Shopping List",
                    items=[
                        "Milk",
                        "Bread",
                        "Eggs"
                    ]
                )
            ]
        )


    with app:
        app.loop.run_until_complete(main())

To-Do Service Messages
-----------------------

Handle to-do completion and task addition service messages:

.. code-block:: python

    from pyrogram import Client, enums

    app = Client("my_account")


    @app.on_message()
    async def todo_service_handler(client, message):
        if message.service == enums.MessageServiceType.TODO_COMPLETIONS:
            print("Tasks completed!")

        if message.service == enums.MessageServiceType.TODO_APPEND_TASKS:
            print("New tasks added!")


    app.run()
