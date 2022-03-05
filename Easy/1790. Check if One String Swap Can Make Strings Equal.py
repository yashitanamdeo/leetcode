# Problem Statement: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2: count += 1
        return (Counter(s1) == Counter(s2)) and (count == 0 or count == 2)