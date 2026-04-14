print("Ця програма виводить останню цифру введеного числа.")

user_number = int(input("Введіть число: "))

last_number = user_number % 10

print(f"\nОстання цифра: {last_number}")