class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def gen_stats(word):
            stats = {}
            for char in word:
                if char not in stats:
                    stats[char] = 0
                stats[char] += 1

            return stats
        return gen_stats(s) == gen_stats(t)
    