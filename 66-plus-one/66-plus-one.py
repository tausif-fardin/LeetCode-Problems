class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        carry = 1       
        i = len(digits)-1
        
        while i>=0:
            
            curr = digits[i]+ carry            
            digits[i] = curr%10           
            carry = curr // 10      
            if not carry:
                 break
            i-=1
        
        if carry:
            digits.insert(0,carry)
        return digits

        