def threeNumberSum(array, targetSum):
    # Write your code here.
    # Using Sliding Pointer O(n^2)
    array.sort()
    results = []
    for i in range(len(array) - 2):
        new_sum = targetSum - array[i]
        low = i + 1
        high = len(array) - 1
        while low < high:
            if (array[low] + array[high]) == new_sum:
                results.append([array[i], array[low], array[high]])
                high -= 1
            elif (array[low] + array[high]) > new_sum:
                high -= 1
            else:
                low += 1
    return results


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

result = threeNumberSum(array, targetSum)

print(result)
