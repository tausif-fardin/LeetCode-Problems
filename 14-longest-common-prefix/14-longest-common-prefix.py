class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        #base condition
        if len(strs) == 0:
            return lcp
        
        #find the min lenght string from the array
        minLength = len(strs[0])
        
        for i in range(1, len(strs)):
            minLength = min(minLength, len(strs[i]))
            
        #loop until the minimum length
        
        for i in range(0, minLength):
            currentChar = strs[0][i]
            
            #check if this character is found in all other strings
            for j in range(0, len(strs)):
                if(strs[j][i] != currentChar):
                    return lcp
            lcp+=currentChar
        return lcp
        
        