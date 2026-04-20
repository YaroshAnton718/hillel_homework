arr1 = [12, 3, 4, 10]
arr2 = [1]
arr3 = []
arr4 = [12, 3, 4, 10, 8]

arr1.insert(0, arr1[len(arr1)-1])
arr1.pop(len(arr1)-1)

arr2.insert(len(arr2), arr2[0])
arr2.pop(0)

if len(arr3) == 0:
    print(arr3)

new_arr = arr4[-1:] + arr4[:-1]

print(new_arr)

print(arr1)
print(arr2)
print(arr4)