# LeetCode: Image Overlap
# Link: https://leetcode.com/problems/image-overlap/
# Language: Python3
# Synced with CodeSync

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):

                overlap = 0

                for r in range(n):
