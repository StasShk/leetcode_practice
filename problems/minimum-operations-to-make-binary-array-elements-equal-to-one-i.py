### https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                ans += 1
                for j in range(i, i + 3):
                    nums[j] ^= 1

        if nums[-1] & nums[-2]:
            return ans
        return -1