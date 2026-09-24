# LeetCode: Smallest Index With Digit Sum Equal to Index
# Link: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
# Language: Python3
# Synced with CodeSync

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        total = 0
        digit = 0
        for i in range(len(nums)):
            total = 0
            num = nums[i]
            if num < 10:
                if num == i:
                    return i
                    
            else:
                while num > 0:
                    digit = num % 10
                    total += digit
                    num = num // 10
                if total == i:
                    return i
        return -1
