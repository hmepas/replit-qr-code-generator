import qrcodeT

# Заполните переменные ниже
name = "Pavel" # Введите свое имя между кавычек
telegram_account = "hmepas" # Введи между кавычек свой аккаунт в Telegram

application_msg = f"Привет, я {name} прошу добавить меня в Кодильню, мой телеграмм http://t.me/{telegram_account}"
qrcodeT.qrcodeT(application_msg)
