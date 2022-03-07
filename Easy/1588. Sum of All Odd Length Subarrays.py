# Problem Statement: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, A):
        n = len(A)
        res = 0
        for l in range(1, n + 1, 2):
            for i in range(n - l + 1):
                res += sum(A[i:i + l])
        return res

# Alternate Solution
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0; freq = 0; n = len(arr)
        for i in range(n):
            freq = freq-(i+1)//2+(n-i+1)//2
            res += freq*arr[i]
        return res
# Explanation: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/919521/python-3-99.78-faster-and-100-less-space