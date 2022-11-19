# Переменные.
program = "Твит в твиттере"
stars = 80
tabs = 5
userText = ""
bestWord = "nigger"
banWords = "хозяин"

# Вывод имени программы в консоль.
print("\t" * tabs, program)
print("*" * stars)

# Ввод данных от пользователя.
userText = input("Введите ваш твит: ")
userText = userText.lower()

if len(userText) >= 280:
    print("Ваш твит слишком длинный!")
elif len(userText) < 280:
    print("Ищем запрещенные слова")

for i in range (0, 110, 10):
    print(i, "%")

if banWords in userText:
    print("В вашем твите есть запрещенные слова!")
    print("Ваш твит не опубликован!")
elif banWords != userText:
    print("В вашем твите нету запрещенных слов!")

if bestWord in userText:
    print("Вам полагается премия в 100.000$ лично от Илона Маска")
    print("Ваш твит опубликован!")
elif bestWord != userText:
    print("Илон Маск не доволен тобой!")


print(userText.lower())




