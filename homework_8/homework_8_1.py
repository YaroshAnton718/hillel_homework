def add_one(some_list):
    i = len(some_list) - 1
    while i >= 0:
        if some_list[i] + 1 == 10:
            some_list[i] = 0
            i -= 1
            continue
        else:
            some_list[i] += 1
            break

    if some_list[0] == 0:
        some_list.insert(0, 1)

    return some_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")