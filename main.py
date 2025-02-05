import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.client.default import DefaultBotProperties
from datetime import datetime
import functions
from files.credentials import *

logging.basicConfig(level=logging.INFO)
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

@dp.message(Command("week_attendants"))
async def week_attendants(message: types.Message):
    week_attendants =  functions.get_week_attendants_list(functions.get_current_week_dates(), functions.get_attendants_list())
    await message.answer(f"<blockquote>{week_attendants}</blockquote>")

@dp.message(Command("current_attendant"))
async def current_attendant(message: types.Message):
    current_attendant = functions.get_current_attendant(functions.get_attendants_list())
    await message.answer(f"<blockquote>{current_attendant}</blockquote>")

async def send_daily_notification():
    while True:
        today_hour, today_minute = datetime.today().hour, datetime.today().minute
        if today_hour == 18 and today_minute == 00:
            current_attendant = functions.get_current_attendant(functions.get_attendants_list())
            await bot.send_message(CHAT_ID, f"<blockquote>{current_attendant}</blockquote>")
            await asyncio.sleep(60)
        await asyncio.sleep(1)

async def main():
    asyncio.create_task(send_daily_notification())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
