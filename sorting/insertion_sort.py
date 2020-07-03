from random import randint

def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1

        array[j] = spam

array = [randint(-10, 10) for i in range(10)]
print(array)

insertion_sort(array)
print(array)
