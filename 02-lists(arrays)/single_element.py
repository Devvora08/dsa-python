# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

def single_el(nums):
    # 1,1,2,2,3,3,4,5,5,6,6,7,7
    # index of odd-even pair changes after single element is present

    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start + (end-start)//2

        # edge cases
        if len(nums) == 1:
            return nums[mid]
        if mid == 0:
            if nums[mid] != nums[mid+1]:
                return nums[mid]
        if mid == len(nums)-1:
            if nums[mid] != nums[mid-1]:
                return nums[mid]

        # main case
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        
        if mid % 2 == 0:
            if nums[mid] == nums[mid+1]:
                start = mid+2
            else:
                end = mid-1
        else:
            if nums[mid] == nums[mid-1]:
                start = mid+1
            else:
                end = mid-1


nums = [3,3,7,7,10,11,11]
print(single_el(nums))