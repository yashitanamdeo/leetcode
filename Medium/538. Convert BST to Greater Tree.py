# Problem Statement: https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root):
        def visit1(root):
            if root:
                visit1(root.left)
                vals.append(root.val)
                visit1(root.right)
        vals = []
        visit1(root)

        self.s = 0
        def visit2(root):
            if root:
                visit2(root.right)
                self.s += vals.pop()
                root.val = self.s
                visit2(root.left)
        visit2(root)

        return root