def select_numbers_basic():
    """Базовый вариант выбора чисел из интервала [1;3]"""
    
    print("=== Выбор чисел из интервала [1;3] ===")
    
    # Ввод трёх целых чисел
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        num3 = int(input("Введите третье целое число: "))
        
        # Создаём список для подходящих чисел
        selected_numbers = []
        
        # Проверяем каждое число
        if 1 <= num1 <= 3:
            selected_numbers.append(num1)
        
        if 1 <= num2 <= 3:
            selected_numbers.append(num2)
            
        if 1 <= num3 <= 3:
            selected_numbers.append(num3)
        
        # Выводим результат
        print(f"\nВведённые числа: {num1}, {num2}, {num3}")
        print(f"Числа из интервала [1;3]: {selected_numbers}")
        print(f"Количество подходящих чисел: {len(selected_numbers)}")
        
    except ValueError:
        print("Ошибка: введите целые числа!")

# Запуск программы
select_numbers_basic()