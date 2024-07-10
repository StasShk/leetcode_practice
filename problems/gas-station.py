### https://leetcode.com/problems/gas-station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        i = 0
        for j in range(l):
            gas[j] -= cost[j]
        if sum(gas) < 0:
            return -1

        while i < l:
            s = 0
            if gas[i] >= 0:
                for j in range(l):
                    p = (i + j) % l
                    s += gas[p]
                    if s < 0:
                        i = max(i, p)
                        break
                else:
                    return i
            i += 1
        return -1
