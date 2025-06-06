# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Date Solved: 06-06-2025
# Topics: Math, HashTable, String

class Solution(object):
    def romanToInt(self, s):
        RomanIntegers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        prev_value = 0

        for i in s[::-1]:
            if RomanIntegers[i] < prev_value:
                value -= RomanIntegers[i]
            else:
                value += RomanIntegers[i]

            prev_value = RomanIntegers[i]

        return value
