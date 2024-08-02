### https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        l = len(nums)
        n = nums.count(1)
        total = sum(nums[:n])
        if l == total or total == 0:
            return 0

        max_w = total

        for i in range(n,l*2):
            total = total + nums[i%l] - nums[(i-n)%l]
            max_w = max(total, max_w)
        return n - max_w
