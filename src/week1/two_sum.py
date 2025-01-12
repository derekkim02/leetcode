class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        
        buff = set()
        for i in range(size):
            if nums[i] in buff:
                for j in range(size):
                    if nums[j] == target - nums[i]:
                        return [j, i]
            diff = target - nums[i]
            buff.add(diff)