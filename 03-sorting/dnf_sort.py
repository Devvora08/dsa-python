def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t


def dnf(nums: list):
    # define the pointers
    low = 0
    mid = 0
    high = len(nums)-1

    # define the spaces for 0, 1,2
    # 0 - 0 -> l-1
    # 1 - l -> mid - 1
    # 2 - high + 1 -> end

    while mid <= high:
        if nums[mid] == 0:
            swap(nums, low, mid)
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            swap(nums, high, mid)
            high -= 1
    
    return nums

nums = [2,2,0,1,2,0,0,1,1,2,0,1,0,2,0,1,2]
print(dnf(nums))