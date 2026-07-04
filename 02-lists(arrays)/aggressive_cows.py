# You are given an array 'arr' consisting of 'n' integers which denote the position of a stall.
# You are also given an integer 'k' which denotes the number of aggressive cows.
# You are given the task of assigning stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible.
# Return the maximum possible minimum distance.

# Ex :
# n = 3
# k = 2
# arr = {1,2,3}
# answer = 2
# Explanation - The max possible min distance will be 2 when 2 cows are placed at positions {1,3}. Here distance between cows is 2.

def isValid(arr,n,k, min_dist):
    cows = 1
    lastPos = arr[0]

    for i in range(n):
        if arr[i] - lastPos >= min_dist:
            cows += 1
            lastPos = arr[i]
        if cows == k: return True
    
    return False

def aggressive_cows(arr, n, k):
    if k>n:  # edge condition where cows > stalls
        return -1
    
    # sort the array
    sorted(arr)

    start = 1
    end = arr[-1] - arr[0]
    min_ans = -1

    while start <= end:
        mid = start + (end-start) // 2

        if isValid(arr,n,k, mid):
            min_ans = mid
            start = mid+1
        else:
            end = mid-1
    
    return min_ans


pos = [2,4,6,8,9]
cows = 3
n = 5

print(aggressive_cows(pos, n, cows))