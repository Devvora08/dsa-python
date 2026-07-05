# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

def product_array(nums):
    # approach - iterate 2 times, create additional array of same size for prefix
    prefix = [0] * len(nums)
    ans = list()
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] * nums[i]
    
    suffix =[0] * len(nums)
    suffix[-1] = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i]
    

    for i in range(len(nums)):
        if i == 0:
            ans.append(suffix[1])
        elif i == len(nums)-1:
            ans.append(prefix[-2])
        else:
            ans.append(prefix[i-1] * suffix[i+1])
    
    return ans


nums = [1,2,3,4]
print(product_array(nums))

    
