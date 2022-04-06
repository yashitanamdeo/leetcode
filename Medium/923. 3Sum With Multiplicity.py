# Problem Statement: https://leetcode.com/problems/3sum-with-multiplicity/

class Solution:
    def threeSumMulti(self, A, T):
        nmap, third, ans = [0 for _ in range(101)], ceil(T / 3) - 1, 0
        for num in A: nmap[num] += 1
        for k in range(min(T,100), third, -1):
            rem = T - k
            half = ceil(rem / 2) - 1
            for j in range(min(rem, k), half, -1):
                i = rem - j
                x, y, z = nmap[i], nmap[j], nmap[k]
                if i == k: ans += x * (x-1) * (x-2) // 6
                elif i == j: ans += x * (x-1) // 2 * z
                elif j == k: ans += x * y * (y-1) // 2
                else: ans += x * y * z
        return ans % 1000000007