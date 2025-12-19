text = input("Введите строку: ")
cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Это палиндром!")
else:
    print("Это не палиндром")