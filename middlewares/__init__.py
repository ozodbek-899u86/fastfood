from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .chek_sub import BigBother

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(BigBother())
