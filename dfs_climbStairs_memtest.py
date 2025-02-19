"""
When a value is calculated for the first time, 
we record it in mem[i] for later use.
When that value needs to be calculated again, 
we can directly retrieve the result from mem[i],
thus avoiding redundant calculations of that subproblem.
"""

class Solution:
    def dfs(self, i: int) -> int:
        """Search"""
        # Known dp[1] and dp[2], return them
        if i == 1 or i == 2:
            return i
        # dp[i] = dp[i-1] + dp[i-2]
        count = self.dfs(i - 1) + self.dfs(i - 2)
        return count

    def climbStairs(self, n: int) -> int:
        """Climbing stairs: Search"""
        return self.dfs(n)
