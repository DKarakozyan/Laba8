# Задача 2 - Последовательность чисел
total = 0
count = 0
print("Вводите числа (0 для завершения):")

while True:
    num = int(input("Число: "))
    if num == 0:
        break
    total += num
    count += 1

print(f"Сумма: {total}")
print(f"Количество: {count}")