# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types, html, F
# from aiogram.filters.command import Command, CommandObject
# from config_reader import config
# from datetime import datetime
#
# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# # bot = Bot(token="6151411579:AAEAjP9IC-vID_OtvVwOaQIbcfiRCmLFV5Q")
# # Диспетчер
# dp = Dispatcher()
#
#
# # Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Hello!")
#
#
# @dp.message(Command("answer"))
# async def cmd_answer(message: types.Message):
#     await message.answer("Это простой ответ")
#
#
# @dp.message(Command("reply"))
# async def cmd_reply(message: types.Message):
#     await message.reply('Это ответ с "ответом"')
#
#
# @dp.message(Command("dice"))
# async def cmd_dice(message: types.Message):
#     await message.answer_dice(emoji="🎲")
#
#
# @dp.message(Command("test"))
# async def any_message(message: types.Message):
#     await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
#     await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")
#
#
# @dp.message(Command("name"))
# async def cmd_name(message: types.Message, command: CommandObject):
#     if command.args:
#         await message.answer(f"Привет, {html.bold(html.quote(command.args))}")
#     else:
#         await message.answer("Введите свое имя после команды /name ")
#
#
# # @dp.message(F.text)
# # async def echo_with_time(message: types.Message):
# #     # Получаем текущее время в часовом поясе ПК
# #     time_now = datetime.now().strftime('%H:%M')
# #     # Создаем подчеркнутый текст
# #     added_text = html.underline(f"Создано в {time_now}")
# #     # Отправляем новое сообщение с добавленным текстом
# #     await message.answer(f"{message.html_text}\n\n{added_text}")
#
#
# @dp.message(F.text)
# async def extract_data(message: types.Message):
#     data = {
#         "url": "eremkin.ru",
#         "email": "eremkin@gmail.com",
#         "code": "eremkin12345",
#     }
#     entities = message.entities or []
#     for item in entities:
#         if item.type in data.keys():
#             # Неправильно
#             # data[item.type] = message.text[item.offset : item.offset+item.length]
#             # Правильно
#             data[item.type] = item.extract_from(message.text)
#     await message.answer(
#         "Вот что я нашел: \n"
#         f"URL: {html.quote(data['url'])} \n"
#         f"E-mail: {html.quote(data['email'])} \n"
#         f"Пароль: {html.quote(data['code'])} \n"
#     )
#
#
# # Запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


def multiply_num(list_numbers: list) -> int:
    result = [list_numbers[number]*list_numbers[number+1] for number in range(len(list_numbers)-1)]
    return result


list_numbers1 = [2, -3, 6]
print(multiply_num(list_numbers1))