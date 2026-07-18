class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # O(n) time | O(1) space
        
        if len(s) != len(t):
            return False
        
        # dictionary of chars
        char_array = [0] * 26

        for i in range(len(s)):
            # get index and char in s and increament value in dict
            s_index = ord(s[i]) - ord('a')
            char_array[s_index] += 1

            # get index and char in t and decrease value in dict
            t_index = ord(t[i]) - ord('a')
            char_array[t_index] -= 1
            
        # check if any value in char array is less than zero
        for val in char_array:
            if val<0:
                return False
        
        return True