# find the sum of maximum subarray

# brute force
def max_subarray_sum(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            curr = 0;
            for k in range(i, j+1):
                curr = curr + nums[k]
            
            max_sum = max(max_sum, curr)

    return max_sum

# kadane's algorithm
def Kadane_subarray_sum(nums):
    # approach - start from first index, if sum value goes below 0, reinitialize max sum to 0
    max_sum = float('-inf')
    curr = 0
    for i in range(len(nums)):
        curr = curr + nums[i]
        max_sum = max(max_sum, curr)
        if curr < 0:
            curr = 0
    
    return max_sum


nums = [1,-5,3,18,-20,400,-5]

print(Kadane_subarray_sum(nums))