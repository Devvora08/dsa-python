# O(n)^2

def swap(nums: list, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t

def bubblesorting(nums):
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[j] < nums[j-1]:
                swap(nums, j, j-1)
    
    return nums
    
nums = [5,7,10,12,1,2,3,4,40]
print(bubblesorting(nums))