### https://leetcode.com/problems/jump-game-ii/description

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        cur = 1
        priv = 0
        step = 0
        max_step = 0

        while True:
            if max_step >= len(nums) :
                return step
            for i in range(priv, cur):
                max_step = max(max_step, i+nums[i]+1)
            step +=1

            cur, priv = max_step, cur