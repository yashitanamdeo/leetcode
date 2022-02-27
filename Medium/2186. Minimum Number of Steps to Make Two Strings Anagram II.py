# Problem Statement: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        char_count = [0] * 26
        for i in range(26):
            char_count[i] = 0
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
        for i in range(len(t)):
            char_count[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if char_count[i] != 0:
                if char_count[i] != 0:
                    count += abs(char_count[i])
        return count