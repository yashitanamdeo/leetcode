# Problem Statement: https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maximum = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if count == 0:
                count += 1
                maximum = nums[i]
            elif maximum == nums[i]:
                count += 1
            else:
                count -= 1
        return maximum
    
# Alternate Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

'''
def majorityElement(self, nums):
        
        # Boyer's Moore Algorithm --> O(1) Space
        
        # We first assume that our first num is the majority element
        # So the count here is 1 as we have seen it 1 times, if the 
        # count in the end is greater than 0 we are sure that this is majority element
        # as if you take count of majority element and subtract sum of all counts of non
        # Majority element, if that count is still positive that it proves that is
        # majority element. We do not need to check count in end over here as we are 
        # sure that there exists a majority element.
        count = 1
        
        # Our Initial guess that this is the majority element
        result = nums[0]
        
        for num in nums[1:]:
            # If the next number is not same as prev
            # and count becomes 0 make this number as majority element and initialize 
            # count to 1 again else just decrease the count
            if num != result:
                # decrease count by 1
                count -= 1
                # Make this element as majority element
                if count == 0:
                    result = num
                    count = 1            
            else:
                # This is same element as previous one.
                count += 1
        
        return result

'''