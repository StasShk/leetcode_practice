### https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        res = []

        cur = TreeNode(-1, left=TreeNode(-1, left=root))
        d = set(to_delete + [-1])

        def f(node):
            if node.left:
                c = node.left
                if c.val in d:
                    node.left = None
                    if c.left and c.left.val not in d:
                        res.append(c.left)
                    if c.right and c.right.val not in d:
                        res.append(c.right)
                f(c)
            if node.right:
                c = node.right
                if c.val in d:
                    node.right = None
                    if c.left and c.left.val not in d:
                        res.append(c.left)
                    if c.right and c.right.val not in d:
                        res.append(c.right)
                f(c)

        f(cur)
        return res
