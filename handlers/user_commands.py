from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.user import reply

from db.database import db
from config_reader import bot_username

router = Router()


@router.message(CommandStart())
async def start(message: Message, bot: Bot):
    
    if not db.get_user(message.from_user.id):

        value = message.text[7:]
        if value != '' and value != message.from_user.id:
            db.update_data(message.from_user.id, value)
            try:
                await bot.send_message(value, f"По вашей ссылке присоединился новый пользователь: {'@'+message.from_user.username if hasattr(message.from_user, 'username') else message.from_user.id}")

            except:
                pass
        else:
            db.update_data(message.from_user.id)

        await message.answer('Вы успешно зарегестрировались в боте!', reply_markup=reply.main)
    
    else:
        await message.answer("Добро пожаловать!", reply_markup=reply.main)
        
        


@router.message(F.text == "Пригласить друга")
async def get_code(message: Message):
    
    await message.answer(
        f"Твоя реферальная ссылка на приглашение:\nhttps://t.me/{bot_username}?start={message.from_user.id}"
    )
    
    
@router.message(F.text == 'Мои рефералы')
async def check_code(message: Message):
    user_id = message.from_user.id

    res = db.count_referrals(user_id)

    await message.answer(f'Общее число рефераллов: {res}')
        
        
