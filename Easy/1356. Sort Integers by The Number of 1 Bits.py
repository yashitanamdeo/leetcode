# Problem Statement: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        brr=[]
        for i in arr:
            brr.append([i, bin(i).replace("0b","").count("1")])
        brr.sort(key = lambda x: x[1])
        ans=[]
        for element, bit_count in brr:
            ans.append(element)

        return ans