# 217. Contains Duplicate
# Approach: Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct.
# Time: ?  Space: ?

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num in nums:
            if counter[num] >= 2:
                return True

        return False

