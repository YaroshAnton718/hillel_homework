lists_for_testing = [[0, 1, 7, 2, 4, 8], [1, 3, 5], [6], []]

for test_list in lists_for_testing:
    test_list_length = len(test_list)

    if test_list_length == 0:
        result = 0
        print(result)
    else:
        sum_of_even_elements = 0
        for i in range(test_list_length):
            if i % 2 == 0:
                sum_of_even_elements += test_list[i]

        result = sum_of_even_elements * test_list[-1]

        print(result)