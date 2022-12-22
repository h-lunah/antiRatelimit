# antiRatelimit
A Python file that prevents your Discord bot Repls from dying because of ratelimits.

## Supported Discord bot modules
- [Hikari with Lightbulb](https://github.com/hikari-py/hikari)
- [Discord.py](https://github.com/Rapptz/discord.py)

## How to use?
- Include `ar.py` in your source tree
- Import the file with `import ar`
- Call `ar.ratelimit_handler()` after your imports
- Call `ar.ratelimit_scanner.start()` in your `on_ready` event 
