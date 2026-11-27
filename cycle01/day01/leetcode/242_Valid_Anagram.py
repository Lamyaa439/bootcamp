# 242. Valid Anagram
# Approach: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Time: ?  Space: ?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            counter = {}
            for char in s:
                counter[char] = counter.get(char, 0) + 1
            
            for char in t:
                if char not in counter or counter[char] == 0:
                    return False
                counter[char] -= 1
            return True
        return False