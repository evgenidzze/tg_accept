import asyncio
import contextlib
import logging

from aiogram.types import ChatJoinRequest
from aiogram import Bot, Dispatcher, F

BOT_TOKEN = '6173620618:AAFNRUg687y6od2ueJENdn5i_KqdYNhSZpE'
CHANNEL_ID = -1001839929273
ADMIN_ID = 397875584


async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    # msg = 'Раді вітати!'
    # await bot.send_message(chat_id=chat_join.from_user.id, text=msg)
    await chat_join.approve()


async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot: Bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id == CHANNEL_ID)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f'[Exception] - {ex}', exc_info=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())