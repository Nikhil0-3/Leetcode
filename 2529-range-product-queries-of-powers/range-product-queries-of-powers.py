from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7

        # Extract powers of 2 from n
        powers = []
        power = 1
        while power < n:
            power <<= 1

        while n > 0:
            if power <= n:
                powers.append(power)
                n -= power
            power >>= 1

        # Reverse powers to match original logic
        powers = powers[::-1]
        size = len(powers)

        # Initialize dp matrix correctly
        dp = [[0] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = powers[i]
            for j in range(i + 1, size):
                dp[i][j] = (dp[i][j - 1] * powers[j]) % mod

        # Process queries
        res = []
        for left, right in queries:
            res.append(dp[left][right])

        return res