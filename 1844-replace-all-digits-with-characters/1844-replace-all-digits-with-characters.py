S ='abcdefghijklmnopqrstuvwxyz'
def shift(a, b):
        return S[S.index(a)+int(b)]
class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            if i%2==0:
                ans+=s[i]
            else:
                ans+=shift(s[i-1],s[i])
        return ans