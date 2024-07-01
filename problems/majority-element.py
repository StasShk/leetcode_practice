### https://leetcode.com/problems/majority-element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #     return Counter(nums).most_common(1)[0][0]

        # More vote algorithm.

        ans = 0
        count = 0

        for i in nums:
            if count == 0:
                ans = i
            if i == ans:
                count += 1
            else:
                count -= 1

        return ans
