class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        
        # split the s over the space(" ")
        s = s.split(" ")   
        
        # if the lengths of pattern and s are not same then return False
        if len(s) != len(pattern):
            return False
        
        for i in range(len(s)):

            pv, sv = "pat"+pattern[i] , "str"+s[i]
            # add the pattern value and s value if its not in hashmap
            if pv not in hashmap:
                hashmap[pv] = i
                
            if sv not in hashmap:
                hashmap[sv] = i
            
            if hashmap[sv] != hashmap[pv]:
                return False

        return True