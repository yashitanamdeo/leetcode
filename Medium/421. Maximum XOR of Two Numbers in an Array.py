# Problem Statement: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        let ni and nj be the numbers such that xor between them produces maximum
        value among other pairs. let m be the max value.

        m = ni ^ nj
        => m ^ nj = (ni ^ nj) ^ nj
        =>        = ni ^ (nj ^ nj) # xor is associative
        =>        = ni ^ 0
        =>        = ni

        so, m ^ nj = ni

        We note that m is 31-bit integer so we guess bits of m and and with each nj,
        we check if the combination of m and nj will produce ni.

        So time complexity becomes O(32N) = O(N)
        :param nums:
        :return:
        """
        m, mask = 0, 0

        for i in range(32)[::-1]:
            mask |= 1 << i
            prefixes = {n & mask for n in nums}

            tmp = m | (1 << i)

            if any(prefix ^ tmp in prefixes for prefix in prefixes):
                m = tmp

        return m