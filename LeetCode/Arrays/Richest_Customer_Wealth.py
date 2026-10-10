# LeetCode: Richest Customer Wealth
# Link: https://leetcode.com/problems/richest-customer-wealth/
# Language: Python3
# Synced with CodeSync

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        arr = []
        for i in range(0, len(accounts)):
            for j in range(0,len(i)):
                arr.append(sum(i[j]))
        return max(arr)
