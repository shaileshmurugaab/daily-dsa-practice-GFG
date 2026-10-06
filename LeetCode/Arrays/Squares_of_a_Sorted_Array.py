# LeetCode: Squares of a Sorted Array
# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Language: Python3
# Synced with CodeSync

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arr = []
        for i in range(0,len(nums)):
            arr.append(nums[i]*nums[i])
        arr.sort()
        return arr
