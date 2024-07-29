### https://leetcode.com/problems/count-number-of-teams

class Solution:
    def numTeams(self, rat: List[int]) -> int:
        l = len(rat)
        res = 0
        for i in range(1,l-1):
            left_smaller, right_smaller = 0, 0
            left_bigger, right_bigger = 0, 0
            for el in rat[:i]:
                if el > rat[i]:
                    left_bigger += 1
                else:
                    left_smaller += 1
            for el in rat[i+1:]:
                if el < rat[i]:
                    right_smaller += 1
                else:
                    right_bigger += 1
            res += (left_smaller * right_bigger) + (right_smaller * left_bigger)
        return res