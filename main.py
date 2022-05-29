from kinopoisk.movie import Movie
import logging
from aiogram import Bot, Dispatcher, executor, types


bot = Bot("5257127516:AAF4e4A90-bI2XSXh1gNMPpw3gZdEsBrbc8")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("KinoPoisk Tg-bot\nВведите название фильма и узнайте его рейтинг\nРазработчик: Герасименко Егор")

@dp.message_handler(lambda message: message.text)
async def message(message: types.Message):
    try:
        movie_list = Movie.objects.search(message.text)
        await message.answer(f"Фильм: {movie_list[0].title}\nРейтинг: {str(movie_list[0].rating)}")
    except:
        await message.answer("Не удалось найти фильм")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)