# алгоритм сортировки слиянием

import random

def merge_sort(array):

    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_array = merge_sort(array[:middle])
    right_array = merge_sort(array[middle:])

    sorted_array =[]
    left_ind, right_ind = 0, 0

    while len(sorted_array) != len(array):
        if left_array[left_ind] > right_array[right_ind]:
            sorted_array.append(right_array[right_ind])
            if right_ind != len(right_array) - 1:
                right_ind += 1
            else:
                sorted_array.extend(left_array[left_ind:])   
        else:
            sorted_array.append(left_array[left_ind])
            if left_ind != len(left_array) - 1:
                left_ind += 1
            else:
                sorted_array.extend(right_array[right_ind:])
    return sorted_array

array = [i for i in range(11)]
random.shuffle(array)
print(array)

sorted_array = merge_sort(array)
print(sorted_array)
