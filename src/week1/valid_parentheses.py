class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        pairing = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in pairing.values():
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif pairing[c] != stack.pop():
                return False

        return len(stack) == 0