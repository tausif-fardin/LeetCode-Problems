class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_map = {}
        s_map = {}
        result = []

        for c in p:
            p_map[c] = p_map.get(c, 0) + 1

        for i in range(len(s)):
            c = s[i]
            s_map[c] = s_map.get(c, 0) + 1

            if i >= len(p):
                leftmost_c = s[i - len(p)]
                if s_map[leftmost_c] == 1:
                    del s_map[leftmost_c]
                else:
                    s_map[leftmost_c] -= 1

            if p_map == s_map:
                result.append(i - len(p) + 1)

        return result