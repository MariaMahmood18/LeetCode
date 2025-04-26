class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_ones = 0
        current_max_ones = 0
        
        for num in nums:
            if num == 1:
                current_max_ones += 1
                if current_max_ones > max_ones:
                    max_ones = current_max_ones
            else:
                current_max_ones = 0
                
        return max_ones
                
        
        