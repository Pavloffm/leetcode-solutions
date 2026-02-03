class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        letters = set()
        for symbol in s:
            if symbol in letters:
                letters.remove(symbol)
                res += 2
            else: letters.add(symbol)
        if len(letters) != 0: res += 1
        return res
