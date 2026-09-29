from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if same length
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)