# Задача 1: Расчет стоимости покупки со скидкой
sum_purchase = float(input("Введите сумму покупки: "))
age = int(input("Введите возраст покупателя: "))
 
discount = 0
if sum_purchase > 100:
    discount += 10
if age >= 65:
    discount += 5
 
final_price = sum_purchase * ((100 - discount) * 0.01)
print(f"Итоговая сумма со скидкой {discount}%: {final_price}\n")
 
# Задача 2: Площадь и периметр круга (из твоего main 6.py)
import math
diameter = float(input("Введите диаметр окружности: "))
choice = int(input("Площадь (1) или Периметр (2)? "))
 
if choice == 1:
    print(f"Площадь: {math.pi * (diameter ** 2) / 4}")
elif choice == 2:
    print(f"Периметр: {math.pi * diameter}")
