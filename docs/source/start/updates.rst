Handling Updates
================

:doc:`Invoking API methods <invoking>` sequentially is one way to use Pyrogram. This page deals with Telegram updates
and how to handle new incoming messages or other events in Pyrogram.


-----

Defining Updates
----------------

Updates are events that happen in your Telegram account (incoming messages, new members join,
bot button presses, etc.), which are meant to notify you about a new specific state that has changed. These updates are
handled by registering one or more callback functions in your app using :doc:`Handlers <../api/handlers>`.

Each handler deals with a specific event and once a matching update arrives from Telegram, your registered callback
function will be called back by the framework and its body executed.

Registering a Handler
---------------------

To explain how handlers work let's examine the one which will be in charge for handling :class:`~pyrogram.types.Message`
updates coming from all around your chats. Every other kind of handler shares the same setup logic and you should not
have troubles settings them up once you learn from this section.

Using Decorators
^^^^^^^^^^^^^^^^

The most elegant way to register a message handler is by using the :meth:`~pyrogram.Client.on_message` decorator:

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")


    @app.on_message()
    async def my_handler(client, message):
        await message.forward("me")


    app.run()

The defined function ``my_handler``, which accepts the two arguments *(client, message)*, will be the function that gets
executed every time a new message arrives.

In the last line we see again the :meth:`~pyrogram.Client.run` method, this time used without any argument.
Its purpose here is simply to automatically :meth:`~pyrogram.Client.start`, keep the Client online so that it can listen
for updates and :meth:`~pyrogram.Client.stop` it once you hit ``CTRL+C``.

Using add_handler()
^^^^^^^^^^^^^^^^^^^

The :meth:`~pyrogram.Client.add_handler` method takes any handler instance that wraps around your defined callback
function and registers it in your Client. It is useful in case you want to programmatically add handlers.

.. code-block:: python

    from pyrogram import Client
    from pyrogram.handlers import MessageHandler


    async def my_function(client, message):
        await message.forward("me")


    app = Client("my_account")

    my_handler = MessageHandler(my_function)
    app.add_handler(my_handler)

    app.run()
