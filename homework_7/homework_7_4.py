def common_elements():
    set_multiples_of_three = set()
    set_multiples_of_five = set()
    for i in range(100):
        if i % 3 == 0:
            set_multiples_of_three.add(i)

        if i % 5 == 0:
            set_multiples_of_five.add(i)

    set_intersection = set_multiples_of_three.intersection(set_multiples_of_five)

    return set_intersection

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')
