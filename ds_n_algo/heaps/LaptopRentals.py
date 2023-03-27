#From AlgoExpert Heaps

def laptopRentals(times):
    # Write your code here.
    sortedTimes = sortArr(times)
    return getTimeOverlaps(sortedTimes)


def sortArr(times):
    return sorted(times, key=lambda x: x[0])


def getTimeOverlaps(sortedTimes):
    minHeap = []
    for timePair in sortedTimes:
        if len(minHeap) == 0:
            minHeap.append(timePair)
        else:
            if minHeap[0][1] <= timePair[0]:
                removeRoot(minHeap)
            insert(timePair, minHeap)
    return len(minHeap)


def removeRoot(heap):
    endIdx = len(heap) - 1
    heap[0], heap[endIdx] = heap[endIdx], heap[0]
    heap.pop()
    sinkDown(0, heap)


def sinkDown(currentIdx, heap):
    leftChildIdx = 2 * currentIdx + 1
    while leftChildIdx < len(heap):
        rightChildIdx = leftChildIdx + 1 if leftChildIdx + 1 < len(heap) else -1
        indexToSwap = -1
        if rightChildIdx != -1:
            indexToSwap = leftChildIdx if heap[leftChildIdx][1] <= heap[rightChildIdx][1] else rightChildIdx
        else:
            indexToSwap = leftChildIdx
        if heap[currentIdx][1] > heap[indexToSwap][1]:
            heap[currentIdx], heap[indexToSwap] = heap[indexToSwap], heap[currentIdx]
        else:
            break


def insert(element, heap):
    heap.append(element)
    siftUp(len(heap) - 1, heap)


def siftUp(currentIdx, heap):
    parentIdx = (currentIdx - 1) // 2
    while parentIdx >= 0:
        if heap[parentIdx][1] > heap[currentIdx][1]:
            heap[parentIdx], heap[currentIdx] = heap[currentIdx], heap[parentIdx]
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
        else:
            break

times = [[0, 5],[2, 4],[4, 7],[5, 7],[9, 20],[3, 15],[6, 10]]
print(laptopRentals(times))
