class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

        steps = 0

        while num != 0: # run loop until num equals zero
            if num % 2 == 0: # check if num is even
                num = num // 2 # divide num by 2
            else: # if num is odd
                num = num - 1
            steps += 1 # incremnet the number of steps = number of times loop runs

        return steps
        