class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s

        maxL = 0
        maxSub = ""
        lenS = len(s)
        for i in range(lenS):
            for j in range(i, lenS+1):
                substring = s[i:j]
                if len(substring) > maxL and self.isPalin(substring) :
                    maxL = len(substring)
                    maxSub = substring
        
        return maxSub


    def isPalin(self, s):
        l, r = 0, len(s)-1

        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True