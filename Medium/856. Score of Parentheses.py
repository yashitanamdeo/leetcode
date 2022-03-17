# Problem Statement: https://leetcode.com/problems/score-of-parentheses/

class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        answer = 0
        for c in s:
            if c == '(':
                stack.append(answer)
                answer = 0
            else:
                answer = stack.pop() + max(1, answer*2)
        return answer 