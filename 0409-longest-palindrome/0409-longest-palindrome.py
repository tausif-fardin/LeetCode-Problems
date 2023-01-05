class Solution:
    def longestPalindrome(self, s: str) -> int:
        letterCounts = {}
        for letter in s:
            if letter in letterCounts:
                letterCounts[letter] += 1
            else:
                letterCounts[letter] = 1
        longestPalindrome = 0
        hasOdd = False
        for letter, count in letterCounts.items():
            if count % 2 == 0:
                longestPalindrome += count
            else:
                hasOdd = True
                longestPalindrome += count - 1
        if hasOdd:
            longestPalindrome += 1
        return longestPalindrome