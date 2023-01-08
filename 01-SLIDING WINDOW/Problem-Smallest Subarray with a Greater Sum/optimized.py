'''
Problem Statement:
    Given an array of positive numbers, and a positive number 'S', 
    find the length of the smallest contiguous subarray whose sum is
    greater than or equal to 'S'. Return 0 if no such subarray exist

    Example: 
        Input [2,1,5,2,3,2], S = 7
        Output = 2
        Explanation: [5,2] = 7

'''

def minLengthSum(array, S):
    #Initialize min
    minLen = len(array)+1
    
    #Define window
    windowStart, windowSum = 0, 0

    #Iterate through the array
    for windowEnd in range(len(array)):
        #add the next elements
        windowSum += array[windowEnd]
       
         
        #if windowSum >= S, grab length of the window. 
        #We will use the while-loop in this case since we need to make sure windowSum < S for each iteration
        while windowSum >= S:
            currentLen = windowEnd-windowStart+1
            minLen = min(minLen, currentLen)
            
            #Shrink window by moving windowStart and subtracting the removed element
            windowSum -= array[windowStart]
            windowStart += 1

        
            
    return minLen

def main():
    myArray = [2,1,5,2,3,2]
    minSum = minLengthSum(myArray, 7)

    print(minSum)
    return

main()