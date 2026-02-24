class Solution:
    letter_numbers = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        def backtracking(index, current):
            if index == len(digits):
                result.append(current)
                return
            digit = digits[index]
            for letter in self.letter_numbers[digit]:
                backtracking(index + 1, current + letter)
        backtracking(0, "")
        return result
