import math

def calculate_expression():
    """Вычисление арифметического выражения"""
    
    print("=== Вычисление арифметического выражения ===")
    print("Формула: Z = (9πt + 10cos(x)) / (√t - |sin(t)|) * e^x")
    print()
    
    try:
        # Ввод переменных с клавиатуры
        x = float(input("Введите значение x: "))
        t = float(input("Введите значение t: "))
        
        # Проверка допустимости значения t
        if t <= 0:
            print("Ошибка: t должно быть положительным числом!")
            return
        
        denominator = math.sqrt(t) - abs(math.sin(t))
        
        # Проверка деления на ноль
        if denominator == 0:
            print("Ошибка: деление на ноль!")
            return
        
        # Вычисление выражения по формуле
        numerator = 9 * math.pi * t + 10 * math.cos(x)
        Z = (numerator / denominator) * math.exp(x)
        
        # Вывод результата с 2 знаками после запятой
        print(f"\nРезультат вычисления:")
        print(f"При x = {x}, t = {t}")
        print(f"Z = {Z:.2f}")
        
    except ValueError:
        print("Ошибка: введите числовые значения!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Основная программа
if __name__ == "__main__":
    calculate_expression()