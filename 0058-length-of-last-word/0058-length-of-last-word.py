class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove any leading or trailing spaces
        s = s.strip()

        # Split the string into a list of words
        words = s.split()

        # Check if the list of words is empty
        if not words:
            return 0

        # Get the last word in the list and return its length
        return len(words[-1])