class Solution:
    def twoSum(self, nums:list, target:int) -> list: 
        size = len(nums)
        if size == 2:
            return [0,1]

        for i in range(size):
            for j in range(1, size):
                if nums[i] + nums[j] == target:
                    return [i,j]
