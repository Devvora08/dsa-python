# approach 1 - cyclic sort
def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t

def findDuplicate(nums: list):
    i = 0
    while i < len(nums):
        originalIdx = nums[i] - 1 # -1 for adjusting to 1 indexed
        if nums[originalIdx] != nums[i]:
            swap(nums, originalIdx, i)
        else:
            i += 1
    
    i = 0
    
    while i < len(nums):
        if nums[i] != i+1:
            return nums[i]
        else: i += 1  
    return -1

# another optimal approach - fast-slow approach
def duplicate(nums: list):
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break
    
    slow = nums[0]
    
    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast # or return slow
    
nums = [1,4,4,2,3]
print(duplicate(nums))
