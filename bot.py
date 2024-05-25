import asyncio
import logging

from handlers import user_commands

from config_reader import bot, dp

logging.basicConfig(level=logging.DEBUG)

async def main():

    dp.include_routers(
        user_commands.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
