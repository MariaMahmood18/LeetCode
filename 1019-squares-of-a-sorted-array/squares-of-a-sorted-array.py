class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        result = [0] * n  # Initialize an array to hold the sorted squared numbers
        
        left, right = 0, n - 1  # Two pointers
        index = n - 1  # Fill result from the back
        
        # Compare the absolute values at the two pointers
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] ** 2
                left += 1
            else:
                result[index] = nums[right] ** 2
                right -= 1
            index -= 1
        
        return result
            
            
                    
                    
            
            