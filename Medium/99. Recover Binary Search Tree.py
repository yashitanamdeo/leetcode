# Problem Statement: https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prevNode = None, None, None # Create three nodes.
        self.inOrder(root) # Calling the function
        self.first.val, self.second.val = self.second.val, self.first.val 
        # Swapping the two elements needed to be swapped
        
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        
        if self.prevNode: # To handle the case of first node, because we make it prev to begin with
            if self.prevNode.val > root.val: # Check property violation
                if not self.first: 
                    self.first = self.prevNode # Found first pair
                self.second = root # If the second pair is found then simply assign the smaller element of the   pair as the second guy, it works for single pair easily, as it wont get             updated again in that case.
                
        self.prevNode = root
        
        self.inOrder(root.right)