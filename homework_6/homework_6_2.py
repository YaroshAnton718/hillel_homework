import sys

user_input_seconds = int(input("Введіть кількість секунд [0; 8640000]: "))

if user_input_seconds < 0 or user_input_seconds > 8640000:
    print("Введене число за межами дозволеного діапазону.")
    sys.exit(1)

minutes, seconds_remainder = divmod(user_input_seconds, 60)
hours, minutes_remainder = divmod(minutes, 60)
days, hours_remainder = divmod(hours, 24)

str_minutes = str(minutes_remainder)
str_seconds = str(seconds_remainder)
str_hours = str(hours_remainder)

if 10 <= days % 100 <= 14:
    print(f"{user_input_seconds} -> {days} днів, {str_hours.zfill(2)}:{str_minutes.zfill(2)}:{str_seconds.zfill(2)}")
elif days % 10 == 1:
    print(f"{user_input_seconds} -> {days} день, {str_hours.zfill(2)}:{str_minutes.zfill(2)}:{str_seconds.zfill(2)}")
elif 2 <= days % 10 <= 4:
    print(f"{user_input_seconds} -> {days} дні, {str_hours.zfill(2)}:{str_minutes.zfill(2)}:{str_seconds.zfill(2)}")
else:
    print(f"{user_input_seconds} -> {days} днів, {str_hours.zfill(2)}:{str_minutes.zfill(2)}:{str_seconds.zfill(2)}")
