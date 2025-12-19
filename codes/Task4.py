# Задача 1 - Цена конфет
price = float(input("Введите цену за 1 кг конфет: "))
print("Количество кг - Стоимость")
for kg in range(1, 11):
    cost = price * kg
    print(f"{kg} кг - {cost:.2f} руб.")