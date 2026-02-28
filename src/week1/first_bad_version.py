# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def search(l, r):
            mid = (l + r) // 2

            midVer = isBadVersion(mid)
            behind = isBadVersion(mid - 1)
            
            if midVer:
                if not behind:
                    return mid
                if mid == 1:
                    return mid

            if not midVer:
                return search(mid + 1, r)
            
            return search(l, mid - 1)

        return search(1, n)