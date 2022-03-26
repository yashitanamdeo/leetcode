# Problem Statement: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Read the binary number from MSB to LSB
        answer = 0
        while head: 
            answer = 2 * answer + head.val 
            head = head.next 
        return answer 