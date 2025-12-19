# Простейшая версия
numbers = []

print("Введите числа (пустая строка для завершения):")
while True:
    num = input()
    if num == "":
        break
    try:
        numbers.append(float(num))
    except:
        print("Ошибка ввода!")

if numbers:
    numbers.sort()
    print("Отсортированный массив:", numbers)
else:
    print("Массив пуст!")