# search in mountain array
# [3,6,8,10,20,15,14,12,11] tar = 8, 
# peak = 20, otuput = 2

def binary_search(nums,st, end, tar, isAsc):
    while st <= end:
        mid = st + (end-st)//2
        if isAsc:
            if tar == nums[mid]: return mid
            elif tar < nums[mid]:
                end = mid-1
            else: st = mid+1
        else:
            if tar == nums[mid]: return mid
            elif tar < nums[mid]:
                st = mid+1
            else:
                end = mid-1
    return -1

def peak(nums):
    s = 0 
    end = len(nums)-1

    while s < end:
        mid = s + (end-s)//2
        
        if nums[mid] < nums[mid+ 1]:
            s = mid+1
        else: end = mid
    return s

def mountain_array(nums, tar):
    peakEl = peak(nums)
    
    idx = -1
    idx = binary_search(nums, 0, peakEl, tar, True)
    if idx == -1:
        idx = binary_search(nums, peakEl+1, len(nums)-1, tar, False)
    
    return idx

nums = [3,10,15,20,18,12,9]
print(mountain_array(nums, 112))