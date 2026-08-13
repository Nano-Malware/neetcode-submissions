class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        j = 0
        while i < len(s) - 1:
            j += abs(ord(s[i + 1]) - ord(s[i]))
            i += 1
        return j