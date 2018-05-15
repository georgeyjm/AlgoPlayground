from random import randint, shuffle

class generate_array:

    def _shuffle(array):
        shuffle(array)
        return array

    def consecutive(start: int, end: int) -> list:
        '''Generates a shuffled, consecutive, non-repetitive array in the given range.'''
        return generate_array._shuffle([i for i in range(start, end + 1)])

    def fixed_range(start: int, end: int, count: int) -> list:
        '''Generates an array containing a specific length of numbers in the given range.'''
        return [randint(start, end) for i in range(count)]

    def few_unique(start: int, levels: int, levelLength: int, levelHeight: int) -> list:
        '''Generates a stair-like array that has few unique values.'''
        array = []
        for val in range(0, levels * levelHeight, levelHeight):
            array += [start + val for i in range(levelLength)]
        return _shuffle(array)

    def nearly_sorted_array(start: int, end: int, count: int, switchCount: int, startWithConsecutive: bool=False) -> list:
        '''Generates an array that is almost sorted.
        If `startWithConsecutive` is `True`, paramater `count` will be ignored.'''
        if not startWithConsecutive:
            array = sorted(generate_array.fixed_range(start, end, count)) # using `sorted` is quite cheating
        else:
            array = list(range(start, end))
        length = len(array)
        if switchCount > length // 2:
            raise ValueError('switchCount is too big')
        switched = []
        for i in range(switchCount):
            chosen = randint(0, length-1)
            while chosen in switched:
                chosen = randint(0, length-1)
            difference = randint(-length // 10, length // 10) if length >= 10 else 1
            other = chosen + difference
            while other < 0 or other >= length or other == chosen or other in switched:
                difference = randint(-length // 10, length // 10) if length >= 10 else 1
                other = chosen + difference
            array[chosen], array[other] = array[other], array[chosen]
        return array

    def reversed(start: int, end: int) -> list:
        '''Generates a reversed consecutive array in the given range.'''
        return list(reversed([i for i in range(start, end)]))


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
