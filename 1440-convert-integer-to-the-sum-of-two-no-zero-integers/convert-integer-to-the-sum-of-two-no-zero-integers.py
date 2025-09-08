class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        l = []
        for i in range(1, n//2 +1):
            a = str(i)
            b = str(n - i)
            if '0' not in a and '0' not in b:
                l.append(int(a))
                l.append(int(b))
                return l