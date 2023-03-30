class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n = len(days)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + costs[0] # 1-day pass for current day
            
            j = i - 1
            while j >= 0 and days[i - 1] - days[j] < 7:
                j -= 1
            dp[i] = min(dp[i], dp[j + 1] + costs[1]) # 7-day pass for current day
            
            j = i - 1
            while j >= 0 and days[i - 1] - days[j] < 30:
                j -= 1
            dp[i] = min(dp[i], dp[j + 1] + costs[2]) # 30-day pass for current day
        
        return dp[n]