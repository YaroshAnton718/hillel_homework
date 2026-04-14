print("Ця програма переводить хвилини в години.")

user_minutes = int(input("Введіть кількість хвилин: "))

hours, minutes = divmod(user_minutes, 60)

print(f"\n{user_minutes} хвилин у годинах: {hours} годин {minutes} хвилин")