### https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        return min(map(sub, nums[-4:], nums[:4]))
