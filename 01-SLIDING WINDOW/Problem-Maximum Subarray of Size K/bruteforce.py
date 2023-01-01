#Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k

#Input: Array [2, 3, 4, 1, 5] and k=2 
#Output: 7

def max_subarray(array, k):
    #initalize maxSum
    maxSum = 0.0

    #iterate through the array that can add k-elements
    for i in range(len(array)-k+1):
        _sum = 0.0 # iterate sum of current loop

        #iterate through the array and add up to k-elements
        for j in range(i, i+k):
            _sum += array[j]

        #compare current sum to max sum
        maxSum = max(maxSum,_sum)

    print(maxSum)

    return

def main():
    myArray = [2,3,4,1,5]
    max_subarray(myArray,2)

    return

main()