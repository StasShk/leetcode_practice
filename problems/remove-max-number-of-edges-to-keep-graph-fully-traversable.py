#### https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description

class UnF:
    def __init__(self, n):
        self.par = [x for x in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = n

    def f(self, i):
        if self.par[i] == i:
            return i
        res = self.f(self.par[i])
        self.par[i] = res
        return res

    def u(self, x, y):
        par_x = self.f(x)
        par_y = self.f(y)

        if par_x == par_y:
            return 0

        if self.rank[par_x] < self.rank[par_y]:
            self.par[par_y] = par_x
        elif self.rank[par_x] > self.rank[par_y]:
            self.par[par_x] = par_y
        else:
            self.par[par_y] = par_x
            self.rank[par_x] = self.rank[par_y] + 1
        self.size -= 1
        return 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        edges.sort(reverse=True, key=lambda x: x[0])

        a_tree = UnF(n)
        b_tree = UnF(n)
        ans = 0

        for ed in edges:
            if ed[0] == 3:

                if a_tree.u(ed[1], ed[2]) | b_tree.u(ed[1], ed[2]):
                    ans += 1

            elif ed[0] == 1:
                ans += a_tree.u(ed[1], ed[2])
            else:
                ans += b_tree.u(ed[1], ed[2])

        if a_tree.size != 1 or b_tree.size != 1:
            return -1
        else:
            return len(edges) - ans
