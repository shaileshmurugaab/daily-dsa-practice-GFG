# LeetCode: Add Digits
# Link: https://leetcode.com/problems/add-digits/
# Language: Python3
# Synced with CodeSync

class Solution:
    def addDigits(self, num: int) -> int:
        i = 0
        temp = 0
        sumi = 0
        if num >= 0 and num <= 9:
            return num
        else:
            num = str(num)
            for i in range(0,len(num)):
                temp = int(num[i])
                sumi += temp
            return sumi
