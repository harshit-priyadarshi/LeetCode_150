"""
Given an unsorted integer array nums, return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example:- nums = [1,2,0]
Output: 3

nums = [3,4,-1,1]
Output: 2   

nums = [7,8,9,11,12]
Output: 1   
"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n:
                correct_index = nums[i] - 1

                if nums[correct_index] == nums[i]:
                    break

                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
