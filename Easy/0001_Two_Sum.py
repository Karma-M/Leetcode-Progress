# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Date Solved: 06-03-2025
# Tags: Array, Brute Force Solution

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]