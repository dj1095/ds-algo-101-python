#From AlgoExpert Heaps



def sortKSortedArray(array, k):
    # Write your code here.
    currentSortedIndex = 0
    heap = buildMinHeap(array[: min(k + 1, len(array))])
    for idx in range(k + 1, len(array)):
        array[currentSortedIndex] = removeRoot(heap)
        currentSortedIndex += 1
        insert(array[idx], heap)
    while len(heap) > 0:
        array[currentSortedIndex] = removeRoot(heap)
        currentSortedIndex += 1
    return array


def buildMinHeap(array):
    size = len(array) // 2
    for i in range(size, -1, -1):
        sinkDown(i, array)
    return array


def sinkDown(currentIdx, array):
    leftChildIdx = 2 * currentIdx + 1
    arraySize = len(array)
    while leftChildIdx >= 0 and leftChildIdx < arraySize:
        rightChildIdx = leftChildIdx + 1 if leftChildIdx + 1 < arraySize else -1
        indexToSwap = -1
        if rightChildIdx != -1:
            indexToSwap = leftChildIdx if array[leftChildIdx] < array[rightChildIdx] else rightChildIdx
        else:
            indexToSwap = leftChildIdx
        if array[currentIdx] > array[indexToSwap]:
            array[currentIdx], array[indexToSwap] = array[indexToSwap], array[currentIdx]
            currentIdx = indexToSwap
            leftChildIdx = 2 * currentIdx + 1
        else:
            break


def removeRoot(array):
    if len(array) == 0:
        return
    endIdx = len(array) - 1
    array[0], array[endIdx] = array[endIdx], array[0]
    removedElement = array.pop()
    sinkDown(0, array)
    return removedElement


def insert(element, array):
    array.append(element)
    siftUp(len(array) - 1, array)


def siftUp(currentIdx, array):
    parentIdx = (currentIdx - 1) // 2
    while parentIdx >= 0:
        if array[currentIdx] < array[parentIdx]:
            array[currentIdx], array[parentIdx] = array[parentIdx], array[currentIdx]
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
        else:
            break



result = sortKSortedArray([3, 2, 1, 5, 4, 7, 6, 5], 3)
print(result)

