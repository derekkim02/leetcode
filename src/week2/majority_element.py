from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        amount = -1
        elem = nums[0]
        for key, value in count.items():
            if value > amount:
                amount = value
                elem = key
        
        return elem
