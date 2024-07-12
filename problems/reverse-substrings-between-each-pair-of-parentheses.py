### https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses

class Solution:
    def reverseParentheses(self, s: str) -> str:
        pos = []
        pair = {}
        l = len(s)

        for i in range(l):
            if s[i] == "(":
                pos.append(i)
            if s[i] == ")":
                j = pos.pop()
                pair[j], pair[i] = i, j

        res = []
        i, d = 0, 1

        while i < l:
            if s[i] in ")(":
                i = pair[i]
                d *= -1
            else:
                res.append(s[i])
            i += d

        return "".join(res)
