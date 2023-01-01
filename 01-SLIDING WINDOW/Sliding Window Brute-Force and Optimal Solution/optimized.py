## Problem Statement
#Given an array, find the average of all sub-arrays of "K" contiguous elements in it.

#     Array = [ 1 , 3 , 2 , 6 , -1 , 4 , 1 , 8 , 2 ] and K=5

#Solution: Instead of iterating through the array, we will add and subtract elements as we slide the window

def sliding_window_optimized(array, k):
    result = [] #Initiate Result
    windowStart, windowEnd, _sum= 0, 0, 0

    # We will create our window starting from 0 and go through the array
    for windowEnd in range(len(array)): #O(n)
        _sum += array[windowEnd] #Sum the element

        
        #If the window is larger than K-Elements, substract the first element and add the next element
        #Since we know that the _sum is the addition of 5 elements, we will add it to the result
        #We will continue this until we hit the last element
        if windowEnd >= k - 1: #O(1)
            average = _sum/k
            result.append(average)

            #We will subtract the first element
            _sum -= array[windowStart]
            #We will increase the start of the window
            windowStart += 1

    return result


def main():
    myArray = [1,3,2,6,-1,4,1,8,2]
    result = sliding_window_optimized(myArray, 5)
    print(result)

    return

main()