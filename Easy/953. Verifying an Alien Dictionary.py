# Problem Statement: https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        for a, b in zip(words, words[1:]):
            i, j, A, B = 0, 0, len(a), len(b)

            while i < A and j < B:
                aOrderIdx = order.index(a[i])
                bOrderIdx = order.index(b[i])
                if aOrderIdx == bOrderIdx:
                    i += 1
                    j += 1
                elif aOrderIdx > bOrderIdx:
                    return False
                else:
                    break

            if i < A and j == B:
                return False
            
        return True