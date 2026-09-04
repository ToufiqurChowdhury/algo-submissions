class Solution:
    def getSum(self, a: int, b: int) -> int:

        MAX = 2147483647
        MIN = -2147483648

        if(a > 0 and b > 0 and a > MAX - b):
            return -1

        if(a < 0 and b < 0 and a < MIN - b):
            return -1
        
        sum = (a + b)
        
        return sum
        """
        mask = 0xFFFFFFFF

        while (b & mask)!=0:
            tmp = (a & b) << 1
            a = a ^ b
            b = tmp
        return (a & mask) if b > 0 else a

        
        """