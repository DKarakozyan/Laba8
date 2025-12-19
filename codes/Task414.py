text = input("Введите строку: ")

# Удаляем все варианты букв 'a'
result = text.replace('a', '').replace('а', '').replace('A', '').replace('А', '')
removed_count = len(text) - len(result)

print(f"Результат: {result}")
print(f"Удалено символов: {removed_count}")