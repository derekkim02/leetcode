from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = Counter(magazine)
        for char in ransomNote:
            counts[char] -= 1
            if counts[char] < 0:
                return False
        
        return True