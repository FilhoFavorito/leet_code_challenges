# TwoSum:

## Question:

* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

* You may assume that each input would have exactly one solution, and you may not use the same element twice.

* You can return the answer in any order.

## Solution

Two variables ```J``` and ```I``` that iterate through the ```nums``` list.  At the end of each ```J``` iteration the code checks if ```J``` and ```I``` positions summed up are equal to the target and if ```J``` and ```I``` are different numbers.

```python
class Solution:
    def twoSum(self, nums:list, target:int) -> list: 
        size = len(nums)
        if size == 2:
            return [0,1]

        for i in range(size):
            for j in range(1, size):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
```