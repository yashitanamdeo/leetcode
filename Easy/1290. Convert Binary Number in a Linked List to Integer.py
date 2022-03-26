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
    
    
'''
For Example:
1101 -> 13

Binary View
0000 * 2 # shift left
0000 + 1 # add bit

0001 * 2 # shift left
0010 + 1 # add bit

0011 * 2 # shift left
0110 + 0 # add bit

0110 * 2 # shift left
1100 + 1 # add bit

1101 # 13

Decimal View
0 * 2 # x2
0 + 1 # add bit

1 * 2 # x2
2 + 1 # add bit

3 * 2 # x2
6 + 0 # add bit

6 * 2 # x2
12 + 1 # add bit

13 # Answer
'''