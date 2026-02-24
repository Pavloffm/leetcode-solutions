class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # def sheet_column_to_number(columnChar: str) -> int:
        #     return ord(columnChar) - 64
        # res = 0
        # for columnChar in columnTitle:
        #     res = res * 26 + sheet_column_to_number(columnChar) 
        # return res
        return sum((ord(columnTitle[i]) - 64) * 26 ** (len(columnTitle) - 1 - i) for i in range(len(columnTitle)))
