def calculator():
    try:
        num1 = float(input("Введіть перше число: "))

        operation = input("Виберіть операцію (+, -, *, /): ")

        num2 = float(input("Введіть друге число: "))

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
            print("Помилка: невідома операція")
    return

    print(f"Результат: {result}")

    if result % 2 == 0:
        print("Результат парний.")
    else:
        print("Результат не парний.")

     except ValueError:
        print("Помилка: введене значення не є числом.")

calculator()
