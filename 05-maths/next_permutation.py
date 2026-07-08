def reverse(nums: list, st: int, end: int):
    i = st
    j = end
    while i < j:
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t
        
        i+= 1
        j-= 1

def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t

def nextPermutation(nums: list[int]):
    pivotNum = -1 
    n = len(nums)
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            pivotNum = i
            break
    
    if pivotNum == -1:
        reverse(nums, 0, n-1)
        return nums
    
    for i in range(n-1, pivotNum, -1):
        if nums[i] > nums[pivotNum]:
            swap(nums, i, pivotNum)
            break
    
    reverse(nums, pivotNum+1, n-1)
    
    return nums


print(nextPermutation([1,2,3]))