### https://leetcode.com/problems/create-binary-tree-from-descriptions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        def f(node):
            if node.val in left:
                lc = TreeNode(left[node.val])
                node.left = lc
                f(lc)
            if node.val in right:
                rc = TreeNode(right[node.val])
                node.right = rc
                f(rc)

        left = {}
        right = {}
        children = set()

        for el in descriptions:
            children.add(el[1])
            if el[2]:
                left[el[0]] = el[1]
            else:
                right[el[0]] = el[1]

        root = TreeNode()
        for el, _, _ in descriptions:
            if el not in children:
                root.val = el
                break

        cur = root
        f(cur)
        return root
