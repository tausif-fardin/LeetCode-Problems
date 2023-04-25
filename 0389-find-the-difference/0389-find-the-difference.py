class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = [0] * 26  # initialize an array to store count of each letter in s
        for ch in s:
            s_count[ord(ch) - ord('a')] += 1  # increment count of the letter
        for ch in t:
            t_count_index = ord(ch) - ord('a')
            if s_count[t_count_index] == 0:  
                return ch
            s_count[t_count_index] -= 1