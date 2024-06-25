### https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips

class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        ans = 0
        buf = 0
        l = len(a)

        for i in range(l):
            if i >= k and a[i - k] > 1:
                buf -= 1
            if not (a[i] + buf) & 1:
                if i + k > l:
                    return -1

                ans += 1
                buf += 1
                a[i] = 2
        return ans
