# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        buf = []

        def f(node, arr):
            if node is None:
                return None
            f(node.left, arr)
            arr.append(node.val)
            f(node.right, arr)

        f(root, buf)

        i, j = 0, len(buf) - 1

        def bin_ins(s, f):
            if s > f:
                return None
            m = s + (f - s) // 2

            left = bin_ins(s, m - 1)
            right = bin_ins(m + 1, f)
            return TreeNode(buf[m], left, right)

        return bin_ins(i, j)