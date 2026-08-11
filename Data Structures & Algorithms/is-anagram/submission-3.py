class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charmap = [0] * 26

        for c in s:
            charmap[ord(c) - ord('a')] += 1
        
        for c in t:
            idx = ord(c) - ord('a')
            charmap[idx] -= 1

            if charmap[idx] < 0:
                return False

        return True
        