# Problem Statement: https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        # While slow moves one step forward, fast moves two steps forward.
        # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
'''
While slow moves one step forward, fast moves two steps forward.
Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
For example, head = [1, 2, 3, 4, 5].
    step 0: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
    step 1: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
    step 2: slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
    end because fast cannot move forward anymore and return [3, 4, 5]
'''