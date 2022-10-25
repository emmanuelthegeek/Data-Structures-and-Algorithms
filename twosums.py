# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


#Using double forloop method
class Solution:
    def twoSum(self, nums:List[int], target:int)->List[int]:
        for a in  range(len(nums) - 1):
            for b in range(a + 1, len(nums)):
                if nums[a] + nums[b] == target:
                    return ([a, b])


#Using Dictionary method
class Solution:
    def twoSum(self, nums:List[int], target:int)->List[int]:
        new_name = {}
        for x, y in enumerate(nums):
            if target - num in new_name:
                return([new_name[target - new_name], x])
            elif num not in new_name:
                new_name[num] = x


        
