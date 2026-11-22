# Задача 1: Шифр «Беззвучный» (замена гласных на дефис)
word7 = input("Введите слово: ")
word8 = ""
for i in word7.lower():
    if i in ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
        word8 += "-"
    else:
        word8 += i
print(f"Результат: {word8}\n")
 
# Задача 2: Числовой код (ASCII-шифрование)
word3 = input("Введите слово: ")
word4 = ""
for i in word3:
    word4 = word4 + str(ord(i)) + " "
print(f"Выход: {word4.strip()}\n")
 
# Задача 3: Вывод чисел от 1 до 5 с помощью while
count = 1
while count <= 5:
    print(f"Число: {count}")
    count += 1
print("Цикл завершен")
