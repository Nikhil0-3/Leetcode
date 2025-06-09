class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_count(prefix, n):
            count = 0
            current = prefix
            next_prefix = prefix + 1
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count

        curr = 1
        k -= 1  # since we already have 1 as the first number

        while k > 0:
            count = get_count(curr, n)
            if count <= k:
                curr += 1
                k -= count
            else:
                curr *= 10
                k -= 1

        return curr
