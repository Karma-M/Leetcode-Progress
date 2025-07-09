# Problem: https://leetcode.com/problems/single-number/
# Difficulty: Easy
# Date Solved: 07-09-25
# Topics: Array, Bit Manipulation

# First Solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) < 2:
                return i

# Second Solution - XOR Solution
def singleNumber(self, nums):
    result = 0  # Base case for XOR

    for i in nums:
        result ^= i  # XOR of all numbers - cancels out all duplicates

    return result