# Problem Statement: https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right, result = 0, len(people) - 1, 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            result += 1
            right -= 1
        return result
'''
Sort people.
For the current heaviest person, we try to let him go with the lightest person.
As all people need to get on the boat.
If the sum of weight is over the limit, we have to let the heaviest go alone.
No one can take the same boat with him.

At the end of for loop, it may happend that i = j.
But it won't change the result
'''