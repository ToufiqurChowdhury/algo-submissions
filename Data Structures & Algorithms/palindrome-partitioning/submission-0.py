class Solution:
    def partition(self, s: str) -> List[List[str]]:

        """
            backtrack

            aab
            ---
            / | \
           a aa  b
         / |  |
        a ab  b
        |
        b

        time: 2^n
        space: O(n)

        """

        res = []
        part = []

        def dfs(i):
            if i == len(s):
                res.append(part[::])
                return res
            
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res

    def isPalin(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        
        return True




        