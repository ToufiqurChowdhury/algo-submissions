class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # algo: sliding win
        # TC: O(n)
        # SC: O(n)

        charSet = set()
        left = 0
        maxlen = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            maxlen = max(maxlen, (right-left)+1)
        
        return maxlen
        