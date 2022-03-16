# Problem Statement: https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index, stack = 0, []
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return not stack