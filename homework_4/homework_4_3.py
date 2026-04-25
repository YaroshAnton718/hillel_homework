import random

test_list = []
for i in range(random.randint(3, 10)):
    test_list.append(random.randint(1,100))

final_list = []
final_list.append(test_list[0])
final_list.append(test_list[2])
final_list.append(test_list[-2])

print(f"Згенерований список (випадкові цілі числа, довжина від 3 до 10): {test_list}")
print(f"Фінальний список (перший, третій елемент та другий із кінця): {final_list}")