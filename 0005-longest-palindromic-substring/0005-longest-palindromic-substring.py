class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # Base cases: all substrings of length 1 and 2 are palindromes
        for i in range(n):
            dp[i][i] = True
            if i < n - 1 and s[i] == s[i+1]:
                dp[i][i+1] = True

        # Fill in the rest of the dp table
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i + k - 1
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

        # Find the longest palindrome
        max_len = 0
        start = end = 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    start = i
                    end = j

        return s[start:end+1]