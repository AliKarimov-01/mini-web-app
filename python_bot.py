from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio

TOKEN = "8054989598:AAHOvxr7tUNarEe8X1msXv-4biwZMmWiQsI"

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):

    builder = InlineKeyboardBuilder()
    builder.button(
        text="Mini Appni ochish",
        web_app=WebAppInfo(url="http://127.0.0.1:8000")
    )

    await message.answer(
        "Mini Appni ochish uchun tugmani bosing:",
        reply_markup=builder.as_markup()
    )


@dp.message(F.web_app_data)
async def webapp_handler(message: types.Message):

    data = message.web_app_data.data   # ← Mana shu muhim joy
    await message.answer(f"Mini Appdan keldi: {data}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
