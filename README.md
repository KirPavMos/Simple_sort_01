# Простые алгоритмы сортировки
# files:
# README.md
# simple_sort_01.py

1. Алгоритм сортировки пузырьком (Bubble Sort)
Алгоритм проходит по списку, сравнивает пары соседних элементов 
и меняет их местами, если они расположены в неправильном порядке. 
Процесс повторяется, пока список не будет отсортирован.
2. Алгоритм сортировки выбором (Selection Sort)
Алгоритм делит список на две части: отсортированную и 
неотсортированную. На каждом шаге находится минимальный элемент 
из неотсортированной части и помещается в конец отсортированной.
3. Алгоритм сортировки вставками (Insertion Sort) (для сравнения)
Алгоритм строит отсортированную часть списка, вставляя каждый новый 
элемент в правильную позицию.
4. Сравнение времени выполнения алгоритмов
Для сравнения воспользуемся модулем timeit.
5. Результаты сравнения:

Bubble Sort: Медленный, особенно на больших данных (O(n²) 
в худшем случае).

Selection Sort: Быстрее пузырьковой, но тоже O(n²).

Insertion Sort: На частично упорядоченных данных работает 
быстрее (O(n) в лучшем случае).

Вывод:
Для небольших списков разница незначительна.
На больших данных лучше использовать более эффективные алгоритмы 
(например, QuickSort, MergeSort).
Insertion Sort часто оказывается быстрее Bubble и 
Selection Sort на почти упорядоченных данных.