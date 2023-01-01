#Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k

#Input: Array [2, 3, 4, 1, 5] and k=2 
#Output: 7

def maxSum_subarray(array, k):
    #Initalize maxSum and windowStart
    windowStart = 0
    maxSum = 0.0
    _sum = 0.0 #Initalize sum

    #We want to iterate through the array
    for i in range(len(array)): #O(n)
        
        #Inside that array, sum all passed through elements
        _sum += array[i]

        #if index is >k, subtract previous element 
        if i >= k-1: #O(1)

            maxSum = max(maxSum,_sum)
            _sum -= array[windowStart]
            windowStart += 1
             

    print(maxSum)

    return

def main():
    myArray = [2,3,4,1,5]
    maxSum_subarray(myArray,2)

    return

main()