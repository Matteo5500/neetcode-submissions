import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_pulita = re.sub(r'[^a-z0-9]', '', s, flags=re.IGNORECASE).lower()

        if s_pulita[::-1] == s_pulita:
            return True
        else:
            return False