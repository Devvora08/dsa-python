# Given an array arr[] and an integer k, where the array represents the boards and each element denotes the length of a board,
# and k painters are available to paint these boards.
# Each unit length of a board takes 1 unit of time to paint. Find the minimum time required to paint all the boards such that each painter paints only contiguous sections of the array.
# A painter can paint boards like [2, 3, 4], [1], or even no board, but cannot paint non-contiguous boards like [2, 4, 5].
# Examples:
# Input: arr[] = [5, 10, 30, 20, 15], k = 3
# Output: 35

def isValid(boards, n,k, minTime):
    painters = 1
    board = 0

    for i in range(n):
        if boards[i] > minTime:
            return False
        
        if board + boards[i] <= minTime:
            board += boards[i]
        else:
            board = boards[i]
            painters = painters+1
    
    if painters > k:
        return False
    else: return True


def painter_partition(boards, n, k):
    if k > n: 
        return -1
    sum = 0
    max_board = float('-inf')
    for i in range(len(boards)):
        sum += boards[i]
        max_board = max(max_board, boards[i])
    
    # range is max board len to sum
    start = max_board
    end = sum
    ans = -1

    while start <= end:
        mid = start + (end-start)//2

        if isValid(boards, n,k, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid+1
    
    return ans
    
print(painter_partition([5, 10, 30, 20, 15], 5, 3))