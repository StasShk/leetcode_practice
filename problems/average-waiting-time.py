### https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        priv = 0
        t = 0
        for s, w in customers:
            priv = max(s, priv) + w
            t += priv - s
        return t / len(customers)
