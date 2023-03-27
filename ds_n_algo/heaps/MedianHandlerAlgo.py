#From AlgoExpert Heaps

# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.minHeap = []
        self.maxHeap = []

    def insert(self, number):
        # Write your code here.
        minh = self.minHeap
        maxh = self.maxHeap
        if len(maxh) == 0:
            maxh.append(number)
            self.median = number
        else:
            if maxh[0] < number:
                minh.append(number)
                self.minhSiftUp(len(minh) - 1, minh)
            else:
                maxh.append(number)
                self.maxhSiftUp(len(maxh) - 1, maxh)
        self.balanceHeaps(maxh, minh)
        if len(maxh) > len(minh):
            self.median = maxh[0]
        elif len(minh) > len(maxh):
            self.median = minh[0]
        else:
            self.median = (maxh[0] + minh[0]) / 2

    def getMedian(self):
        return self.median

    def minhSiftUp(self, currentIdx, array):
        parentIdx = (currentIdx - 1) // 2
        while parentIdx >= 0 and parentIdx < len(array):
            parentIdx = (currentIdx - 1) // 2
            if parentIdx >=0 and array[parentIdx] > array[currentIdx]:
                array[parentIdx], array[currentIdx] = array[currentIdx], array[parentIdx]
                currentIdx = parentIdx
            else:
                break

    def minhSiftDown(self, currentIdx, array):
        while (len(array) > currentIdx >= 0):
            leftChildIdx = 2 * currentIdx + 1
            rightChildIdx = leftChildIdx + 1
            idxToSwap = -1
            if rightChildIdx < len(array) and ((array[currentIdx] > array[leftChildIdx]) or (array[currentIdx] > array[rightChildIdx])):
                idxToSwap = leftChildIdx if array[leftChildIdx] < array[rightChildIdx] else rightChildIdx
            elif leftChildIdx < len(array) and (array[currentIdx] > array[leftChildIdx]):
                idxToSwap = leftChildIdx
            if idxToSwap != -1:
                array[currentIdx], array[idxToSwap] = array[idxToSwap], array[currentIdx]
                currentIdx = idxToSwap
            else:
                break

    def maxhSiftDown(self, currentIdx, array):

        while (len(array) > currentIdx >= 0):
            leftChildIdx = 2 * currentIdx + 1
            rightChildIdx = leftChildIdx + 1
            idxToSwap = -1
            if rightChildIdx < len(array) and (
                    (array[currentIdx] < array[leftChildIdx]) or (array[currentIdx] < array[rightChildIdx])):
                idxToSwap = leftChildIdx if array[leftChildIdx] > array[rightChildIdx] else rightChildIdx
            elif leftChildIdx < len(array) and (array[currentIdx] < array[leftChildIdx]):
                idxToSwap = leftChildIdx
            if idxToSwap != -1:
                array[currentIdx], array[idxToSwap] = array[idxToSwap], array[currentIdx]
                currentIdx = idxToSwap
            else:
                break

    def maxhSiftUp(self, currentIdx, array):
        parentIdx = (currentIdx - 1) // 2
        while parentIdx >= 0 and parentIdx < len(array):
            parentIdx = (currentIdx - 1) // 2
            if parentIdx >= 0 and array[parentIdx] < array[currentIdx]:
                array[parentIdx], array[currentIdx] = array[currentIdx], array[parentIdx]
                currentIdx = parentIdx
            else:
                break

    def balanceHeaps(self, maxh, minh):
        maxHeapLength = len(maxh)
        minHeapLength = len(minh)
        if (maxHeapLength > minHeapLength and (maxHeapLength - minHeapLength) >= 2):
            ele = self.removeRootElement(maxh, self.maxhSiftDown)
            minh.append(ele)
            self.minhSiftUp(len(minh) - 1, minh)
        elif (maxHeapLength < minHeapLength and (minHeapLength - maxHeapLength) >= 2):
            ele = self.removeRootElement(minh, self.minhSiftDown)
            maxh.append(ele)
            self.maxhSiftUp(len(maxh) - 1, maxh)

    def removeRootElement(self, heap, siftFn):
        heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
        ele = heap.pop()
        siftFn(0, heap)
        return ele


handler = ContinuousMedianHandler()
handler.insert(5)
handler.insert(10)
handler.insert(100)
handler.insert(200)
handler.insert(6)
handler.insert(13)
handler.insert(14)
handler.insert(50)
handler.insert(51)
handler.insert(52)
handler.insert(1000)
handler.insert(10000)
handler.insert(10001)
handler.insert(10002)
handler.insert(10003)
handler.insert(10004)
handler.insert(75)
print(handler.median)


