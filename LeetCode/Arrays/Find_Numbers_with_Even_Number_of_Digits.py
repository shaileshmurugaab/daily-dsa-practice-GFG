# LeetCode: Find Numbers with Even Number of Digits
# Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Language: Python3
# Synced with CodeSync

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        arr = []
temp  = 0
for i in range(0,len(nums)):
    temp = str(nums[i])
    arr.append(len(temp))
print(arr)
temp = 0
for i in range(0,len(arr)):
    if arr[i] % 2 == 0:
        temp += 1
print(temp)
