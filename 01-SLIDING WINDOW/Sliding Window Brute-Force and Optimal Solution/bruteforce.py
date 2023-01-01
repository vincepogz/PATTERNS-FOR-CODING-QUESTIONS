#Define main function
def sliding_window(K, arr):
    result = [] # Initialize empty array for result

    # Define up to which index can add up to K-Element
    for i in range(len(arr)-K+1): #O(n)
        _sum = 0.0  # Initalize int variable

        # Loop through the array of K-Elements
        for j in range(i, i+K): #O(n)
            _sum += arr[j] # Add the element passed through up to K

        # Find the average of the sum and add it to the result
        result.append(_sum/K) 
    
    return result

# Define main function
def main():
    my_array = [1,3,2,6,-1,4,1,8,2]
    result = sliding_window(5,my_array)
    print ("Averages of subarrays of size K: " + str(result))

# Run main function
main()