# Задание 1: Шифр «Задом наперёд» (Реверс)
word = input("Введите слово или фразу: ")
print(f"Слово наоборот: {word[::-1]}\n")
 
# Задание 2: Шифр «Вставка-шпион» (Шум)
word1 = input("Введите слово для шифра звездочками: ")
word2 = ""
for i in word1:
    if i != " ":
       word2 += i + "*"
    else:
        word2 += i + " "
print(f"Результат: {word2}\n")
 
# Задание 3: Упрощенный шифр Цезаря (Сдвиг на 1)
word5 = input("Введите слово для шифра Цезаря: ")
word6 = ""
for i in word5:
    word6 = word6 + chr(ord(i) + 1)
print(f"Зашифрованное слово: {word6}\n")
 
# Работа со встроенными методами строк
string1 = "Hello World"
print(f"Длина строки: {len(string1)}")
print(f"Верхний регистр: {string1.upper()}")
print(f"Нижний регистр: {string1.lower()}")
print(f"Замена буквы: {string1.replace('H', 'h')}")
print(f"Срез слова: {string1[0:5]}")
