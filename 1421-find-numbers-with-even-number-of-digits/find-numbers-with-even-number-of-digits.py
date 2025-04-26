class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        even_number_digits = 0
        digits = 0
        
        for num in nums:
            while num:
                num = num // 10
                digits += 1
                
            if digits % 2 == 0:
                even_number_digits += 1
            digits = 0
                
        return even_number_digits

        # return sum(1 for num in nums if len(str(num)) % 2 == 0)
