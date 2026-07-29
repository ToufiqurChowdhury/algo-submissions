class Solution:
    def isHappy(self, n: int) -> bool:

        numset = set()
        hnum = 0
        cur = n

        while True:
            while cur:
                digit = cur % 10
                cur = cur // 10
                hnum += digit * digit

            if hnum == 1:
                return True
            
            if hnum in numset:
                return False
            
            numset.add(hnum)
            cur = hnum
            hnum = 0


        