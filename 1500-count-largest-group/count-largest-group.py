class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """

        def num_sum(num):
            sum = 0
            while num > 0:
                sum += num % 10 # last digit
                num //= 10 # removes last digit
            return sum

        groups = {} 

        for i in range(1, n+1):
            s = num_sum(i)
            if s in groups:
                groups[s] +=1
            else:
                groups[s] = 1

        max_size = max(groups.values())
        return sum(1 for g in groups.values() if g == max_size)


        



        