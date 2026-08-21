'''
Missing Number: Given an array nums containing n distinct numbers in the range [0, n]
 return the only number in the range that is missing from the array.
'''
from pyparsing import nums


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        n=len(nums)
        missing=n
        for i in range(n-1):
            missing ^= i ^ nums[i]
        return missing
print(Solution().missingNumber([3, 0, 1]))