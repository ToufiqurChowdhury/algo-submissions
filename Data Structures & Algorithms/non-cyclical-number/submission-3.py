class Solution:
    def isHappy(self, n: int) -> bool:

        # numset = set()
        # hnum = 0
        # cur = n

        # while True:
        #     while cur:
        #         digit = cur % 10
        #         cur = cur // 10
        #         hnum += digit * digit

        #     if hnum == 1:
        #         return True
            
        #     if hnum in numset:
        #         return False
            
        #     numset.add(hnum)
        #     cur = hnum
        #     hnum = 0

        visit=set()

        while n not in visit:
            visit.add(n)

            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False

    def sumOfSquares(self, n):
        output = 0

        while n:
            digit = n%10
            digit = digit ** 2
            output += digit
            n = n // 10

        return output 

        