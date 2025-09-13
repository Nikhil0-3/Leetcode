class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = set('aeiou')
        freq = Counter(s)
        max_vowel = 0
        for ch in vowel :
            if ch in freq:
                max_vowel = max(max_vowel,freq[ch])

        max_cons = 0
        for ch in freq:
            if ch not in vowel:
                max_cons = max(max_cons,freq[ch])

        return max_vowel + max_cons

        

