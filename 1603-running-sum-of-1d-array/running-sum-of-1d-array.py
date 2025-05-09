class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = [] # new array initialization to store the running sum values

        current_sum = 0

        for num in nums:
            current_sum += num
            running_sum.append(current_sum)

        return running_sum