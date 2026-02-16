class Solution:
    def mySqrt(self, n: int) -> int:
        if n < 2: return n
        x = 1 << (n.bit_length() + 1 >> 1)
        while True:
            y = (x + n // x) >> 1
            if y >= x: return x if x * x <= n else x - 1
            x = y
