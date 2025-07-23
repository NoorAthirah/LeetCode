class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = []

        for i in range(len(nums)):
            if nums[i] != val:
                result.append(nums[i])
        
        for i in range(len(result)):
            nums[i] = result[i]
        
        return(len(result))
        