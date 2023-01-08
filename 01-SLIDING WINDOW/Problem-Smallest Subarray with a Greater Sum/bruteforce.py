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

def subarrayLength(array, S):
    #Initiate length
    minLength = len(array)+1

    #Iterate through the array
    for i in range(len(array)):
    #Iniatiate current sum, and array
        currSum = 0.0
        arraySum = []
        
        #Iterate to the next elements, grab each sum per visit
        for j in range(i,len(array)):
            
            currSum += array[j]
            arraySum.append(array[j])
        #If the sum is >=S, compare the length
            if currSum >= S:
                print(arraySum)
                minLength = min(minLength, len(arraySum))
                break
                

    return minLength

def main():
    myArray = [2,1,5,2,3,2]
    minSum = subarrayLength(myArray, 7)

    print(minSum)
    return

main()
