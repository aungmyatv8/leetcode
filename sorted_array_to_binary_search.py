def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        print(mid, low, high, arr[mid])
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1


arr = [ 2, 3, 4, 10, 20, 30, 35, 40 ]

result = binary_search(arr, 4)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")