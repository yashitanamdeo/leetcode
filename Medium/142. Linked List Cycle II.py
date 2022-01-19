# Problem Statement: https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head 
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None  # if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head    

'''
slow moves 1 step at a time, fast moves 2 steps at a time.
when slow and fast meet each other, they must be on the cycle
    x denotes the length of the linked list before starting the circle
    y denotes the distance from the start of the cycle to where slow and fast met
    C denotes the length of the cycle
    when they meet, slow traveled (x + y) steps while fast traveled 2 * (x + y) steps, and the extra distance (x + y) must be a multiple of the circle length C
        note that x, y, C are all lengths or the number of steps need to move.
        head, slow, fast are pointers.
        head moves x steps and arrives at the start of the cycle.
so we have x + y = N * C, let slow continue to travel from y and after x more steps, slow will return to the start of the cycle.
At the same time, according to the definition of x, head will also reach the start of the cycle after moving x steps.
so if head and slow start to move at the same time, they will meet at the start of the cycle, that is the answer.
'''