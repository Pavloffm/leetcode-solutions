class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def create_lps(needle: str):
            lps, l, i = [0] * len(needle), 0, 1
            while i < len(needle):
                if needle[i] == needle[l]:
                    l += 1
                    lps[i] = l
                    i += 1
                else:
                    if l != 0:
                        l = lps[l - 1]
                    else:
                        lps[i] = 0
                        i += 1

            return lps

        lps = create_lps(needle)
        i = j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle): return i - j
            else:
                if j != 0: j = lps[j-1]
                else: i += 1

        return -1
