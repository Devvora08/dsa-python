def swap(nums : list, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t

def insertionSorting(nums):
    # approach - sort in chunks
    for i in range(len(nums)):
        for j in range(i, 0, -1):
           if nums[j] < nums[j-1]:
               swap(nums, j, j-1)
    
    return nums

nums = [5,7,10,12,1,2,3,4,40]
print(insertionSorting(nums))