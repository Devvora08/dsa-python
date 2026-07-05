# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

def pivot(nums):
    s = 0
    e = len(nums)-1

    while s <= e:
        mid = s + (e - s)//2

        if mid < e and nums[mid] > nums[mid+1]:
            return mid
        if mid > s and nums[mid] < nums[mid-1]:
            return mid-1
        
        # special case - s == e == mid
        if nums[mid] == nums[s] and nums[mid] == nums[e]:
            if s < e and nums[s] > nums[s+1]:
                return s
            s += 1

            if e > s and nums[e] < nums[e-1]:
                return e-1
            e -= 1
        
        # shift s, e pointers
        if nums[mid] > nums[s] or (nums[mid] == nums[s] and nums[mid] > nums[e]):
            s = mid+1
        else: e = mid-1
    
    return -1 

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

def search_duplicated_rotated_array(nums, tar):
    pivot_point = pivot(nums)

    if tar == nums[pivot_point]: return True

    if pivot_point == -1:
        idx = binary_search(nums, 0, len(nums)-1, tar)
        if idx == -1:
            return False
        else: return True
    
    if tar < nums[pivot_point] and tar < nums[-1]:
        # 2nd half
        idx = binary_search(nums, pivot_point+1, len(nums)-1, tar)
        if idx == -1: return False
        else: return True
    else:
        idx = binary_search(nums,0, pivot_point, tar)
        if idx == -1: return False
        else: return True

print(search_duplicated_rotated_array([8,9,9,2,2,2,4,4,7,8,8], 1))