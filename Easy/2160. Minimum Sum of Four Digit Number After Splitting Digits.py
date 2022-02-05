# Problem Statement: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        x = [int(a) for a in str(num)]
        mini = min(x)
        x.remove(min(x))
        smini = min(x)
        x.remove(min(x))
        #print(mini,smini)
        #print(x)
        mini = str(mini) + str(x[0])
        num1 = int(mini)
        #print(num1)
        smini = str(smini) + str(x[1])
        num2 = int(smini)
        #print(num2)
        return num1 + num2