from aiogram import Bot


async def sender(user_id, username, bot: Bot):
    await bot.send_message(user_id, f'Ваш друг {username} успешно вступил по ссылке!')