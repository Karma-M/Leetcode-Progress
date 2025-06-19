# Problem: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Date Solved: 06-19-25
# Topics: String, Trie

class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""

        for i in range(len(strs[0])):
            char = strs[0][i] # get the character at index i of the first word

            for word in strs[1:]:  # checks against all other words
                if i >= len(word) or word[i] != char: # breaks if i is outside of range or if characters don't match
                    return prefix
            prefix += char

        return prefix
