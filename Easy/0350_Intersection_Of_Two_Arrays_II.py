# Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Difficulty: Easy
# Date Solved: 07-10-25
# Topics: Array, Hash Table

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dictionary = {}
        result = []

        # Find shorter array
        if len(nums1) < len(nums2):
            shorter, longer = nums1, nums2
        else:
            shorter, longer = nums2, nums1

        # Create dictionary from shorter array
        for number in shorter:
            if number in dictionary:
                dictionary[number] += 1
            else:
                dictionary[number] = 1

        # Iterate over longer list and build result
        for number in longer:
            if number in dictionary:
                result.append(number)
                dictionary[number] -= 1
                if dictionary[number] == 0:
                    del dictionary[number]

        return result