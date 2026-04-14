print("Ця програма виводить у стовпчик цифри, із яких складається введене число.")

user_number = int(input("Введіть число: "))

first_digit, next_step_number = divmod(user_number, 1000)
second_digit, next_step_number = divmod(next_step_number, 100)
third_digit, next_step_number = divmod(next_step_number, 10)
fourth_digit, next_step_number = divmod(next_step_number, 1)

print("\nЦифри числа у стовпчик: ")
print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)