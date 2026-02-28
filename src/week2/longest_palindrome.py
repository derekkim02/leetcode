from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        counts = Counter(s)
        res = 0
        foundOdd = False

        for value in counts.values():
            if value % 2 == 0:
                res += value
                continue

            if not foundOdd:
                foundOdd = True
            res += value - 1
        
        if foundOdd:
            res += 1
        return res