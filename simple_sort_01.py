# Простые алгоритмы сортировки

# Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сравнение времени выполнения алгоритмов
import timeit
import random

def compare_sorting_algorithms():
    test_list = random.sample(range(1, 10001), 100)

    # Измерение времени выполнения каждого алгоритма
    bubble_time = timeit.timeit(lambda: bubble_sort(test_list.copy()), number=1)
    selection_time = timeit.timeit(lambda: selection_sort(test_list.copy()), number=1)
    insertion_time = timeit.timeit(lambda: insertion_sort(test_list.copy()), number=1)

    print(test_list)
    print(f"Bubble Sort Time: {bubble_time:.6f} sec")
    print(f"Selection Sort Time: {selection_time:.6f} sec")
    print(f"Insertion Sort Time: {insertion_time:.6f} sec")


compare_sorting_algorithms()





