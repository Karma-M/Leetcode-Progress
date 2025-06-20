# Problem: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Date Solved: 06-20-25
# Topics: String, Stack


class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        # Last open bracket must close before any others
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)  # Appends only if it's an open bracket
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                # False if closing bracket doesn't match last opened bracket
                # Or if list is empty before pair closes
                return False

        # True if all brackets have been closed
        return len(stack) == 0