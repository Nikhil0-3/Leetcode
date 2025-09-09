class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[1] = 1
        pref[1] = 1

        for i in range(2, n + 1):
            L = max(1, i - forget + 1)
            R = i - delay
            if R >= L:
                dp[i] = (pref[R] - pref[L - 1]) % MOD
            pref[i] = (pref[i - 1] + dp[i]) % MOD

        start = max(1, n - forget + 1)
        ans = (pref[n] - pref[start - 1]) % MOD
        return ans