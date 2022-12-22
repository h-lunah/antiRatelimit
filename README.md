# antiRatelimit
A Python file that prevents your Discord bot Repls from dying because of ratelimits.

## Supported Discord bot modules
- [Hikari with Lightbulb](https://github.com/hikari-py/hikari)
- [Discord.py](https://github.com/Rapptz/discord.py)

<sup><sub>Make sure to install Busybox in your Repl, otherwise this won't work.</sub></sup>

## How to use?
- Include `ar.py` in your source tree
- Import the file with `import ar`
- Call `ar.ratelimit_handler()` after your imports
- Call `ar.ratelimit_scanner.start()` in your `on_ready` event 
