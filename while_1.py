# Переменные.
program = "Вход в систему Python-разработчик"
stars = 80
tabs = 5
password = ""
login = ""
level = 0

# Работа с циклом while и ввод данных от пользоваетля.
while not login:
    login = input("Login: ")

while not password:
    password = input("Password: ")

if login == "Admin" and password == "uva4mwc44":
    level = 5
elif login == "CEO_Admin" and password == "uva44mwc4":
    level = 10


if level:
    print("Здравствуйте, ", login)
    print("Ваш уровень доступа: ", level)