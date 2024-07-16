### https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-anothe

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        r = []

        def f(goal, node):
            if node.val == goal:
                return True
            else:
                if node.left:
                    if f(goal, node.left):
                        r.append("L")
                        return True
                if node.right:
                    if f(goal, node.right):
                        r.append("R")
                        return True
            return False

        f(startValue, root)
        r.reverse()

        s, r = r, []
        f(destValue, root)
        r.reverse()
        j = 0
        for i in range(min(len(s), len(r))):
            if s[i] != r[i]:
                break
            j += 1
        d = r[j:]
        s = ["U"] * (len(s) - j)
        return "".join(s + d)
