### https://leetcode.com/problems/maximum-total-importance-of-roads/description/

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        roads = list(chain(*roads))
        cities = {x: 0 for x in range(n)} | Counter(roads)

        ans = 0
        for i, x in enumerate(sorted(cities.items(), key=lambda x: x[1])):
            ans += (i + 1) * x[1]

        return ans