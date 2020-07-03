from random import randint

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        left = []
        mid = []
        right = []
        pivot = array[len(array)//2]
        for num in array:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)
        return quick_sort(left) + mid + quick_sort(right)

array = [randint(0, 50) for i in range(10)]

sort_array = quick_sort(array)

print(array)
print(sort_array)

