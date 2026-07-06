# approach is to find the max element every time, and insert it to end

def getMax(nums: list, s, e):
    maxEl = s
    for i in range(s, e+1):
        if nums[i] > nums[maxEl]:
            maxEl = i
    
    return maxEl

def swap(nums : list, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t

def selectionsorting(nums: list):
    for i in range(len(nums)):
        s = 0
        end = len(nums) - i - 1

        maxEl = getMax(nums, 0, end)
        swap(nums, end, maxEl)
    
    return nums

nums = [5,7,10,12,1,2,3,4,40]
print(selectionsorting(nums))
