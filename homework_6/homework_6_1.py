import string

user_input = input("Введіть діапазон англійських літер (<літера>-<літера>): ")

first_letter_index = string.ascii_letters.index(user_input[0])

second_letter_index = string.ascii_letters.index(user_input[2])

if first_letter_index > second_letter_index:
    print("Перша літера за значенням ASCII коду більша за другу літеру.")
else:
    print(f"Результат: {string.ascii_letters[first_letter_index: second_letter_index + 1]}")