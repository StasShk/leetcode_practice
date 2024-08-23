### https://leetcode.com/problems/fraction-addition-and-subtraction/

import math
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        m = re.findall('.?\d+/\d+', expression)
        n, d = 0, 1

        for el in m:
            x, y = map(int, el.split("/"))
            z = math.lcm(d, y)
            n = n * (z // d) + x * (z // y)
            d = z
        if (z := math.gcd(n, d)) > 1:
            n = n // z
            d = d // z

        return '{0}/{1}'.format(n, d)
