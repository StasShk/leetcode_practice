## https://leetcode.com/problems/find-the-winner-of-the-circular-game/?envType=daily-question&envId=2024-07-08

class Solution:
    ##    def findTheWinner(self, n: int, k: int) -> int:
    ##        fr = [i+1 for i in range(n)]
    ##        i = 0
    ##        while len(fr) > 1:
    ##            i = ((i + k-1)%(len(fr)))
    ##            fr.pop(i)

    ##        return fr[0]

    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        for pl in range(2, n + 1):
            i = (i + k) % pl
        return i + 1
