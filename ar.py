import os
import sys

import requests  # alternatively you can use httpx, whatever suits you best

# uncomment the import module corresponding to the module you are using in your discord bot
# from lightbulb.ext import tasks  # hikari + lightbulb
# from discord.ext import tasks  # discord.py


def ratelimit_handler():
    print("Checking if we are ratelimited...")
    headers = requests.head("https://discord.com/api/v10").headers
    if headers.get("Retry-After"):
        print("Ratelimited, assigning a new IP...")
        os.system("busybox reboot")  # make sure to install busybox in your repl
        sys.exit(1)
    print("Not ratelimited")
    return


# uncomment the function corresponding to the module you are using in your discord bot
# @tasks.task(m=1)  # hikari + lightbulb
# async def ratelimit_scanner():
#     headers = requests.head("https://discord.com/api/v10").headers
#     if headers.get("Retry-After"):
#         print("Ratelimited, now rebooting...")
#         os.execl(sys.executable, sys.executable, *sys.argv)


# @tasks.loop(minutes=1)  # discord.py
# async def ratelimit_scanner():
#     headers = requests.head("https://discord.com/api/v10").headers
#     if headers.get("Retry-After"):
#         print("Ratelimited, now rebooting...")
#         os.execl(sys.executable, sys.executable, *sys.argv)
