# code to find the majority element from a given list of numbers

def find_maj(nums):
    # approach - use hashmap to track the frequence of each
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else: 
            dict[i] = 1
    max_fre = -10000

    for freq in dict:
        max_fre = max(max_fre, dict[freq])
    
    for i in dict:
        if dict[i] == max_fre:
            return i


def majorityElement(nums):
    # use moore's voting algoritm [o(n) : TC]
    maj_el = -1000
    freq = 0
    for i in range(len(nums)):
        if(freq == 0):
            maj_el = nums[i]
            freq += 1
        elif nums[i] == maj_el:
            freq += 1
        else:
            freq -= 1
    return maj_el


print(majorityElement([1,1,2,3,3,3,3,3,3,4,3,2,2,2,1,3,4,4]))


