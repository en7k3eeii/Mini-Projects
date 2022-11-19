import random

word = input("Введите слово: ")

max = len(word)
min = -len(word)

for i in range(10):
    position = random.randint(min, max)
    print("word[", position, "] = ", word[position])