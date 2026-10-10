class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result1 = sorted(s)
        result2 = sorted(t)
        if result1 == result2:
            return True
        else:
            return False
