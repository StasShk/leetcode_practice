### https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.s = 0

        def f(node):
            if node.right:
                f(node.right)
            node.val += self.s
            self.s = node.val
            if node.left:
                f(node.left)

        cur = root
        f(cur)

        return root
