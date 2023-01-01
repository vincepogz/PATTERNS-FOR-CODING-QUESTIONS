#Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size 'k'

# [2, 1, 5, 1, 3, 2] and k=3

def subarray_sum(array, k):
    result=[]

    #We will iterate through the array that can add k-elements
    for i in range(len(array)-k+1): #O(n)
        _sum = 0.0

        #We will iterate through the array starting at i and up to k elements
        for j in range(i,i+k): #O(n)
            _sum += array[j]
        
        #Grab the result and add it to the list
        result.append(_sum)

    print(result)
    return result

def main():
    myArray = [2,1,5,1,3,2]
    subarray_sum(myArray,3)

    return

main()