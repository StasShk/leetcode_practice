### https://leetcode.com/problems/spiral-matrix-iii/submissions/1349070944

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [(rStart, cStart)]

        step = 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        while len(res) < rows * cols:

            for _ in range(step):
                rStart += directions[i % 4][0]
                cStart += directions[i % 4][1]

                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append((rStart, cStart))
            if i % 2:
                step += 1
            i += 1

        return res
