class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        max_wealth = 0
        wealth = 0

        for i in range(len(accounts)): 
            for j in range(len(accounts[i])): 
                wealth += accounts[i][j]
            if wealth > max_wealth:
                max_wealth = wealth
            wealth = 0

        return max_wealth

        