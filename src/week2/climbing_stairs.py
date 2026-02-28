class Solution(object):
    memo = {
        1: 1,
        2: 2,
    }
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.memo.get(n):
            return self.memo.get(n)

        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]