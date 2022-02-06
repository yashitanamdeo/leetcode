# Problem Statement: https://leetcode.com/problems/sort-even-and-odd-indices-independently/

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        else:
            evensorted = []
            oddsorted = []
            for i in range(len(nums)):
                if i%2 == 0:
                    evensorted.append(nums[i])
                else:
                    oddsorted.append(nums[i])
            evensorted.sort()
            oddsorted.sort(reverse=True)
            
            evenindex = 0
            oddindex = 0
            for i in range(len(nums)):
                if i%2==0:
                    nums[i] = evensorted[evenindex]
                    evenindex += 1
                else:
                    nums[i] = oddsorted[oddindex]
                    oddindex += 1
        return nums