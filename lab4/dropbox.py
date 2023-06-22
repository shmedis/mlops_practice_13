import dropbox

# Укажите ваш API-ключ или токен авторизации
TOKEN = "sl.Bg2HgFjtIiJ2QCVTkwfwVpC-k3uzFsj8Otw5B3GISHBuLdIPi-4siqVnUU8rlYK2vYDZwBk6k2HPhUfOh1oRpHYWWoqWZegSxTCf2LCbdvpJ5laHMqWoz0b5r_Ncp1cJrXCWQGc"

# Создайте соединение с Dropbox
dbx = dropbox.Dropbox(TOKEN)

# Получите информацию о вашем аккаунте Dropbox
account_info = dbx.users_get_current_account()
print(account_info.name.display_name)

# Загрузите файл на Dropbox
with open("local_file.txt", "rb") as f:
    dbx.files_upload(f.read(), "/remote_file.txt")