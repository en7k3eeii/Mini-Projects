import random

print("*" * 10, "Угадай число", "*" * 10)

print("ИИ будет загадывать число от 1 до 10. Попробуй угадать число.Введите 0 для выхода")

answer = 1;
score = 0;
i = 0

while answer: # {
    if answer == 0:
        break
    randomNumber = random.randint(1, 10)
    answer = int(input("Число загадано. Попробуй угадать: "))
    if answer == randomNumber:
        score = score + 1
        print("Правильно")
    else:
        print("Неправильно :(")
    i = i + 1
# }

print("Всего ты отгадал чисел ", score, " из ", i)
print("Пока!")

