class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        original = x
        reverse = 0
        while original > 0:
            reverse = reverse * 10 + original % 10
            original //= 10
        return reverse == x
