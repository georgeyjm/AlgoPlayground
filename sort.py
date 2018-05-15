def bubble_sort(array: list) -> (list, int):
    array = array[:] # create a copy
    length = len(array)
    comparisons = 0

    for i in range(length - 1):
        for j in range(length - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            comparisons += 1
    return array, comparisons

def insertion_sort(array: list) -> (list, int):
    array = array[:] # create a copy
    length = len(array)
    comparisons = 0

    for i in range(length):
        for j in range(i):
            if array[j] > array[i]:
                array.insert(j, array[i])
                del array[i + 1]
            comparisons += 1
    return array, comparisons

def selection_sort(array: list) -> (list, int):
    array = array[:] # create a copy
    length = len(array)
    comparisons = 0

    for i in range(length - 1):
        minIndex = i
        for j in range(i + 1, length):
            if array[j] < array[minIndex]:
                minIndex = j
            comparisons += 1
        array[i], array[minIndex] = array[minIndex], array[i]
    return array, comparisons

def merge_sort(array: list, comparisons: int=0) -> (list, int):
    length = len(array)
    if length == 1:
        return array, comparisons
    result = []
    middleIndex = length // 2
    left, comparisons = merge_sort(array[:middleIndex], comparisons)
    right, comparisons = merge_sort(array[middleIndex:], comparisons)
    leftPointer, rightPointer = 0, 0

    while leftPointer < len(left) and rightPointer < len(right):
        if left[leftPointer] > right[rightPointer]:
            result.append(right[rightPointer])
            rightPointer += 1
        else:
            result.append(left[leftPointer])
            leftPointer += 1
        comparisons += 1
    result += left[leftPointer:] + right[rightPointer:]
    return result, comparisons

def quick_sort(array: list, comparisons: int=0) -> (list, int):
    length = len(array)
    if length == 0:
        return array, comparisons
    pivot = array[0]
    smaller, larger, same = [], [], []

    for element in array:
        if element < pivot:
            smaller.append(element)
            comparisons += 1
        elif element > pivot:
            larger.append(element)
            comparisons += 1
        else:
            same.append(element)
    smaller, comparisons = quick_sort(smaller, comparisons)
    larger, comparisons = quick_sort(larger, comparisons)
    result = smaller + same + larger
    return result, comparisons
