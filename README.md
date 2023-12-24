<p align="center">
    <a href="https://github.com/pyrogrammod/pyrogrammod">
        <img src="https://docs.pyrogram.org/_static/pyrogram.png" alt="Pyrogram" width="128">
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br>
    <a href="https://pyrogrammod.github.io">
        Homepage
    </a>
    •
    <a href="https://pyrogrammod.github.io">
        Documentation
    </a>
    •
    <a href="https://pyrogrammod.github.io/releases">
        Releases
    </a>
    •
    <a href="https://t.me/pyrogrammod">
        News
    </a>
</p>

## Pyrogram

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

``` python
from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")


app.run()
```

**Pyrogram** is a modern, elegant and asynchronous [MTProto API](https://docs.pyrogram.org/topics/mtproto-vs-botapi)
framework. It enables you to easily interact with the main Telegram API through a user account (custom client) or a bot
identity (bot API alternative) using Python.

### Support

If you'd like to support Pyrogram, you can consider:

- [Become a GitHub sponsor](https://github.com/sponsors/delivrance).
- [Become a LiberaPay patron](https://liberapay.com/delivrance).
- [Become an OpenCollective backer](https://opencollective.com/pyrogram).

### Key Features

- **Ready**: Install Pyrogram with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/pyrogram/tgcrypto), a high-performance cryptography library written in C.  
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

``` bash
pip3 install https://github.com/PyrogramMod/PyrogramMod/archive/refs/heads/main.zip
```

### Resources

- The docs contain lots of resources to help you get started with Pyrogram: https://docs.pyrogram.org.
- Seeking extra help? Come join and ask our community: https://t.me/pyrogram.
- For other kind of inquiries, you can send a [message](https://t.me/haskell) or an [e-mail](mailto:dan@pyrogram.org).

### Copyright & License

- Copyright (C) 2017-2022 Dan <<https://github.com/delivrance>>
- Licensed under the terms of the [GNU Lesser General Public License v3 or later (LGPLv3+)](COPYING.lesser)

### INFO

- 📕 Official Repo: https://github.com/pyrogram/pyrogram
- 🗞 News: https://t.me/pyrogram
- 💭 Support Group: https://t.me/pyrogramchat
- 📚 Docs: https://docs.pyrogram.org
------------------------------------------------------------
- 📕 Un-Official Repo: https://github.com/PyrogramMod/PyrogramMod/
- 🗞 News: https://t.me/PyroGramMod
- 💭 Support Group: https://t.me/pyrogramodchat
- 📚 Docs: https://pyrogrammod.readthedocs.io/
------------------------------------------------------------

- Check out the docs at https://docs.pyrogram.org to learn more about Pyrogram, get started right
away and discover more in-depth material for building your client applications.
- Join the official channel at https://t.me/pyrogram and stay tuned for news, updates and announcements.
