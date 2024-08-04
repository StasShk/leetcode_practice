### https://leetcode.com/problems/word-search-ii/description/

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        ans = []
        m = len(board)
        n = len(board[0])

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def insert(s):
            cur = root
            for w in s:
                if w not in cur:
                    cur[w] = {}
                cur = cur[w]
            cur['*'] = s

        for w in words:
            insert(w)

        def search(x, y, trie):
            s = board[x][y]
            cur = trie[s]

            if '*' in cur:
                ans.append(cur.pop('*'))
            board[x][y] = '$'

            for dx, dy in directions:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    if board[x + dx][y + dy] in cur:
                        search(x + dx, y + dy, cur)
            board[x][y] = s
            if not cur:
                trie.pop(s)

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    print(board[i][j], root)

                    search(i, j, root)
        return ans
