# here is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

def binary_search(nums,start, end, tar):
    # generic binary search
    while start <= end:
        mid = start + (end-start)//2
        
        if tar == nums[mid]:
            return mid
        elif tar < nums[mid]:
            end = mid-1
        else: start = mid+1
    return -1

def search_pivot(nums):
    # function to search the pivot point - starting point of array 
    s = 0
    end = len(nums)-1

    while s<end:
        mid = s + (end-s)//2
        
        if nums[mid] > nums[end]:
            s = mid+1
        else:
            end = mid
    return s
    

def search(nums, target):
    starting = search_pivot(nums)

    if target >= starting and target <= nums[-1]:
        return binary_search(nums, starting, len(nums)-1, target)
    else: return binary_search(nums, 0, starting-1, target)

    return -1

print(search([7,8,0,2,3,6], 3))