# __main__.py
import sys
import asyncio
import importlib
from pyrogram import idle
from pyrogram.types import BotCommand
from config import OWNER_ID
from shizuchat import LOGGER, shizuchat
from shizuchat.modules import ALL_MODULES


async def anony_boot():
    try:
        await shizuchat.start()
    except Exception as ex:
        LOGGER.error("Failed to start shizuchat: %s", ex)
        sys.exit(1)

    # Import modules after bot started (safe)
    for all_module in ALL_MODULES:
        importlib.import_module(f"shizuchat.modules.{all_module}")
        LOGGER.info(f"Imported module: {all_module}")

    # Set bot commands (best-effort)
    try:
        await shizuchat.set_bot_commands([
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Help menu"),
            BotCommand("ping", "Check bot status"),
            BotCommand("shipping", "Couples of the day"),
            BotCommand("rankings", "User leaderboard"),
        ])
        LOGGER.info("Bot commands set.")
    except Exception as ex:
        LOGGER.warning("Could not set bot commands: %s", ex)

    LOGGER.info(f"@{shizuchat.username} started.")
    try:
        await shizuchat.send_message(int(OWNER_ID), f"{shizuchat.mention} is online.")
    except Exception:
        LOGGER.info("Could not notify owner; ensure OWNER_ID is correct.")

    await idle()


if __name__ == "__main__":
    # asyncio.run creates and manages the loop safely
    asyncio.run(anony_boot())
