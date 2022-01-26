# Problem Statement: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        st1, st2 = [], []
        res = []
        
        while root1 != None or root2 != None or len(st1) > 0 or len(st2) > 0:
            while root1 != None:
                st1.append(root1)
                root1 = root1.left
            while root2 != None:
                st2.append(root2)
                root2 = root2.left
            if len(st2) == 0 or (len(st1) > 0 and st1[-1].val <= st2[-1].val):
                root1 = st1.pop()
                res.append(root1.val)
                root1 = root1.right
            else:
                root2 = st2.pop()
                res.append(root2.val)
                root2 = root2.right
        return res