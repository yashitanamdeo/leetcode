# Problem Statement: https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = []
        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]
                max_wealth.append(wealth)
        return max(max_wealth)

        # return max(sum(acc) for acc in accounts)
        # return max(map(sum, accounts))

# Alternate Solution
'''
def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for i in accounts:
            wealth.append(sum(i))
        return max(wealth)
'''