from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    sortednums = []
    for i, value in enumerate(nums):
        sortednums.append([value, i])    
    sortednums = sorted(sortednums)
    left = 0 
    right = len(nums) -1
    while left < right:
        if sortednums[left][0] + sortednums[right][0] > target:
            right -= 1
        elif sortednums[left][0] + sortednums[right][0] < target:
            left += 1
        else:
            return [sortednums[left][1], sortednums[right][1]]
            

nums = [2,7,11,15]
target = 9
print(twoSum(nums=nums, target=target))

