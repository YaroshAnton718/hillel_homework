lists_for_testing = [[0, 1, 0, 12, 3],
                     [0],
                     [1, 0, 13, 0, 0, 0, 5],
                     [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]]

for test_list in lists_for_testing:
    number_of_zeros = test_list.count(0)
    list_without_zeros = []
    for el in test_list:
        if el != 0:
            list_without_zeros.append(el)

    list_with_trailing_zeros = list_without_zeros.copy()
    for j in range(number_of_zeros):
        list_with_trailing_zeros.append(0)

    print(list_with_trailing_zeros)