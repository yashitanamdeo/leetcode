# Problem Statement: https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, s: str) -> str:
        dic = {"(al)":"al", "()":"o","G":"G"}
        tmp = ""
        result = ""
        for i in range(len(s)):
            tmp += s[i]
            if(tmp in dic):
                result += dic[tmp]
                tmp = ""
        return result