# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Date Solved: 06-05-2025
# Topics: Math

## Original Solution
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        list_1 = []
        new_string = str(x)
        counter = 0

        for i in new_string:
            list_1.append(i)

        list_2 = list_1[:]
        list_1.reverse()

        for i in (range(len(list_1))):
            if list_1[i] == list_2[i]:
                counter += 1
            elif list_1[i] != list_2[i]:
                return False
        return (counter >= 1)

## Optimized Solution
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]