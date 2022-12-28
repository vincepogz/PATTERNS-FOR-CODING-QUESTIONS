#Define main function
def sliding_window(K, arr):
    result = [] # Initialize empty array for result

    # Shrink array up to "K" elements and pass through that each element
    for i in range(len(arr)-K+1):
        _sum = 0.0  # Initalize int variable

        # Loop through the array of K-Elements
        for j in range(i, i+K):
            _sum += arr[j] # Add the element passed through

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