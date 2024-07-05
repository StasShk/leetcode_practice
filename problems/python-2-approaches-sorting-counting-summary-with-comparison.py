### https://leetcode.com/problems/h-index/solutions/4928640/python-2-approaches-sorting-counting-summary-with-comparison

class Solution:
    def hIndex(self, cit: List[int]) -> int:
        l = len(cit)

        cit.sort()
        priv = cit[0]

        for i in range(l):
            if cit[i] >= l - i:
                return l - i
            else:
                priv = cit[i]
        return min(priv, l)
