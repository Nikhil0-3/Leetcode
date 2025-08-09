class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n <= 0):
            return False
        if (n == 1):
            return True
        while(n>0):
            if n == 1:
                return True
            if (n%2 != 0):
                return False
            n /= 2
        return True