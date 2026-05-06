user_input_number = int(input("Введіть ціле число: "))
further_number = user_input_number
while further_number > 9:
    list_of_numbers = []
    integer_part, remainder = divmod(further_number, 10)
    list_of_numbers.append(remainder)
    while integer_part > 0:
        integer_part, remainder = divmod(integer_part, 10)
        list_of_numbers.append(remainder)

    multiplier = 1
    for number in list_of_numbers:
        multiplier = multiplier * number

    further_number = multiplier

print(f"{user_input_number} -> {further_number}")