from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
ADMINS = ['659237008', 659237008]
IP = env.str("ip")  # Xosting ip manzili
CHANNELS = ['@ITCenterBagdad',]