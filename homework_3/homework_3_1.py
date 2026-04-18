print("Простий калькулятор, який виконує прості математичні дії із двома числами.")

number_1 = float(input("Введіть перше число: "))
number_2 = float(input("Введіть друге число: "))
operator = input("Введіть математичну дію (+, -, *, /): ")

if operator == "+":
    result = number_1 + number_2
    print(f"\n{number_1} + {number_2} = {result}")
elif operator == "-":
    result = number_1 - number_2
    print(f"\n{number_1} - {number_2} = {result}")
elif operator == "*":
    result = number_1 * number_2
    print(f"\n{number_1} * {number_2} = {result}")
elif operator == "/":
    if number_2 == 0:
        print("\nНа 0 ділити не можна.")
    else:
        result = number_1 / number_2
        print(f"\n{number_1} / {number_2} = {result}")
# Вирішив ще додати перевірку на правильне введення математичної дії.
else:
    print("\nНе вірно введено математичну дію.")
