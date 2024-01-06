Welcome to PyrogramMod
===================

.. raw:: html

    <div align="center">
        <a href="/">
            <div class="pyrogram-logo-index"><img src="_static/pyrogram.png" alt="Pyrogram"></div>
            <div class="pyrogram-text pyrogram-text-index">Pyrogram Mod</div>
        </a>
    </div>

    <p align="center">
        <b>Telegram MTProto API Framework for Python</b>

        <br>
        <a href="https://pyrogrammod.github.io">
            Homepage
        </a>
        •
        <a href="https://github.com/pyrogram/pyrogram">
            Development
        </a>
        •
        <a href="https://t.me/pyrogram">
            News
        </a>
    </p>

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")


    @app.on_message(filters.private)
    async def hello(client, message):
        await message.reply("Hello from Pyrogram!")


    app.run()

**Pyrogram** is a modern, elegant and asynchronous :doc:`MTProto API <topics/mtproto-vs-botapi>` framework.
It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot identity
(bot API alternative) using Python.

Support
-------

If you'd like to support Pyrogram, you can consider:

- `Become a GitHub sponsor <https://github.com/sponsors/delivrance>`_.
- `Become a LiberaPay patron <https://liberapay.com/delivrance>`_.
- `Become an OpenCollective backer <https://opencollective.com/pyrogram>`_.

How the Documentation is Organized
----------------------------------

Contents are organized into sections composed of self-contained topics which can be all accessed from the sidebar, or by
following them in order using the :guilabel:`Next` button at the end of each page.
You can also switch to Dark or Light theme or leave on Auto (follows system preferences) by using the dedicated button
in the top left corner.

Here below you can, instead, find a list of the most relevant pages for a quick access.

First Steps
^^^^^^^^^^^

.. hlist::
    :columns: 1

    - :doc:`Quick Start <intro/quickstart>`: Overview to get you started quickly.
    - :doc:`Invoking Methods <start/invoking>`: How to call Pyrogram's methods.
    - :doc:`Handling Updates <start/updates>`: How to handle Telegram updates.
    - :doc:`Error Handling <start/errors>`: How to handle API errors correctly.

API Reference
^^^^^^^^^^^^^

.. hlist::
    :columns: 1

    - :doc:`Pyrogram Mod Client <api/client>`: Reference details about the Client class.
    - :doc:`Available Methods <api/methods/index>`: List of available high-level methods.
    - :doc:`Available Types <api/types/index>`: List of available high-level types.
    - :doc:`Enumerations <api/enums/index>`: List of available enumerations.
    - :doc:`Bound Methods <api/bound-methods/index>`: List of convenient bound methods.

Meta
^^^^

.. hlist::
    :columns: 1

    - :doc:`Pyrogram FAQ <faq/index>`: Answers to common Pyrogram questions.
    - :doc:`Support Pyrogram <support>`: Ways to show your appreciation.

.. toctree::
    :hidden:
    :caption: Introduction

    intro/quickstart
    intro/install

.. toctree::
    :hidden:
    :caption: Getting Started

    start/setup
    start/auth
    start/invoking
    start/updates
    start/errors
    start/examples/index

.. toctree::
    :hidden:
    :caption: API Reference

    api/client
    api/methods/index
    api/types/index
    api/bound-methods/index
    api/enums/index
    api/handlers
    api/decorators
    api/errors/index
    api/filters

.. toctree::
    :hidden:
    :caption: Topic Guides

    topics/use-filters
    topics/create-filters
    topics/more-on-updates
    topics/client-settings
    topics/speedups
    topics/text-formatting
    topics/synchronous
    topics/smart-plugins
    topics/storage-engines
    topics/serializing
    topics/proxy
    topics/scheduling
    topics/mtproto-vs-botapi
    topics/debugging
    topics/test-servers
    topics/advanced-usage
    topics/voice-calls

.. toctree::
    :hidden:
    :caption: Meta

    faq/index
    support

.. toctree::
    :hidden:
    :caption: Telegram Raw API

    telegram/functions/index
    telegram/types/index
    telegram/base/index
