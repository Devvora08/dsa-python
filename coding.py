def binary_search(arr, target) :
    st = 0
    end = len(arr) - 1

    while st<=end:
        mid = st + (end-st) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            st = mid + 1
    
    return -1

data = [1,2,5,29,45, 50]
print(binary_search(data, 29))