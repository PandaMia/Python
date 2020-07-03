from random import randint

def selection_sort(array):

    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
                
        array[idx_min], array[i] = array[i], array[idx_min]

array = [randint(-10, 10) for i in range(10)]
print(array)

selection_sort(array)
print(array)
