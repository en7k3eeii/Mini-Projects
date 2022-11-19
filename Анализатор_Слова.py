# Переменные.
program = "Анализатор слова"              # Имя программы вывадиемое в консоль.
vowels = 0                                # Кол-во гласных в слове.
consonats = 0                             # Кол-во согласных в слове.
word = 0                                 # Слово пользователя.
stars = 80                                # Кол-во звездочек.
tabs = 5                                  # Кол-во отступов(Табуляции).

# Вывод имени в программу.
print("\t" * tabs, program)
print("*" * stars)

# Ввод данных от пользователя.
word = input("Введите слово: ")

allVovels = "аоиеыэюя"

# Цикл for и оператов if
for i in word:
    letter = i.lower()
    if letter in allVovels:
        vowels += 1
    else:
        consonats += 1

print("Длина слова: ", len(word))
print("Кол-во гласных:",vowels,"\nКол-во: согласных:",consonats,"\n")