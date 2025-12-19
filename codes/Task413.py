# Простейшая версия
n = int(input("Количество элементов: "))

numbers = []
for i in range(n):
    num = float(input(f"Элемент {i+1}: "))
    numbers.append(num)

total = 0
print("Элемент -> Сумма")
for i in range(n):
    total += numbers[i]
    print(f"{numbers[i]} -> {total}")

print(f"Общая сумма: {total}")