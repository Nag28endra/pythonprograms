def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapsort(array):
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

    return array
print(heapsort([21,22,12,33,4,32]))