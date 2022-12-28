def sliding_window(K, arr):
    result = []
    for i in range(len(arr)-K+1):
        _sum = 0.0
        for j in range(i, i+K):
            _sum += arr[j]
        result.append(_sum/K)
    return result

def main():
    my_array = [1,3,2,6,-1,4,1,8,2]
    result = sliding_window(5,my_array)
    print ("Averages of subarrays of size K: " + str(result))

main()