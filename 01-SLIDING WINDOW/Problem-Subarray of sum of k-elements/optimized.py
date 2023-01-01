#Given an array of positive numbers and a positive number 'k', find the sum of each subarray of k contigious elements
# [2, 1, 5, 1, 3, 2] and k=3

def sum_subarray(array, k):
    #we want to intialized the result list
    windowStart, _sum = 0, 0
    result = []

    #we will iterate through the array, and add each elements
    for windowEnd in range(len(array)): #O(n)
        _sum += array[windowEnd]

    #if window is >k, shink window by subtracting the right-most element
        if windowEnd >= k-1: # O(1)
            result.append(_sum)
            _sum -= array[windowStart]
            windowStart += 1
            
    #grab the result and add to the list

    print(result)

    return result


def main():
    myArray = [2,1,5,1,3,2]
    sum_subarray(myArray,3)
    return

main()