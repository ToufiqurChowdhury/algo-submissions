class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        parts = []

        def backtrack(i):
            if len(parts) == 4:
                if i == len(s):
                    result.append(".".join(parts))
                return
            
            # Try 1, 2, or 3 digits
            for j in range(i, min(i+3, len(s))):
                part = s[i:j+1]

                # leading zero
                if len(part) > 1 and part[0] == "0":
                    break
                
                # in range 255
                if int(part) > 255:
                    break
                
                parts.append(part)
                backtrack(j+1)
                parts.pop()
            
        backtrack(0)
        return result 
        