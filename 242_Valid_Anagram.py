def isAnagram(self, s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    for l in set(s):  # loop count <= 26
        if s.count(l) != t.count(l):
            return False

    return True
