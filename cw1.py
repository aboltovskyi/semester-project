def calculator():
    try:
        # Запитуємо перше число
        num1 = float(input("Введіть перше число: "))

        # Запитуємо операцію
        operation = input("Виберіть операцію (+, -, *, /): ")

        # Запитуємо друге число
        num2 = float(input("Введіть друге число: "))

        # Виконання операції
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Помилка: ділення на нуль!")
                return
            result = num1 / num2
        else:
            print("Помилка: невідома операція!")
            return

        # Виводимо результат
        print(f"Результат: {result}")

        # Перевірка на парність
        if result % 2 == 0:
            print("Результат парний.")
        else:
            print("Результат непарний.")

    except ValueError:
        print("Помилка: введене значення не є числом.")


calculator()