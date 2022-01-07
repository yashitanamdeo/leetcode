# Problem Statement: https://leetcode.com/problems/linked-list-random-node/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def __init__(self, head):
        self.nodes = []  # convert linked list to a list, cost O(N) Space and O(N) Time
        while head:
            self.nodes.append(head.val)
            head = head.next

    def getRandom(self):  # cost O(1) Time
        return random.choice(self.nodes)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()