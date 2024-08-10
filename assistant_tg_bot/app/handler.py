from aiogram.types import Message
from aiogram.filters import CommandStart, CommandObject
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, CallbackQuery
from aiogram import F, Router
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import ollama

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.bot.send_message(chat_id=1338310078, text=f'@{message.chat.username}')
    await message.answer('...')

    
@router.message(F.text)
async def hello(message: Message):
    user_input = message.text
    await message.answer(ollama.generate(model='llama3.1', prompt=user_input))
