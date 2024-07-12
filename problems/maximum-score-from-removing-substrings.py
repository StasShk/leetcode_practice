### https://leetcode.com/problems/maximum-score-from-removing-substrings

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        res = 0

        c = [("ab", x), ("ba", y)]
        c.sort(key=lambda e: e[1], reverse=True)

        for ss, rq in c:
            buf = []
            for el in s:
                if buf and el == ss[1] and buf[-1] == ss[0]:
                    buf.pop()
                    res += rq
                else:
                    buf.append(el)
            s = "".join(buf)
        return res
