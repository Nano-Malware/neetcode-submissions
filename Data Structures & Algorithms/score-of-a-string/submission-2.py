class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        j = 0
        for i in range(len(s) - 1):
            j += abs(ord(s[i]) - ord(s[i + 1]))
        return j