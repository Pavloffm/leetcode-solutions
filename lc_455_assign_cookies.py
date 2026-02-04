class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        while j <= len(s) - 1 and i <= len(g) - 1:
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i
