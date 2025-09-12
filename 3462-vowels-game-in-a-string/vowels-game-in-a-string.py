class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return sum(1 for c in s if c in "aeiou") != 0