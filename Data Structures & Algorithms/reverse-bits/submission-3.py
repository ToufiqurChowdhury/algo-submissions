class Solution:
    def reverseBits(self, n: int) -> int:
        """
        out = 0
        for i in range(32):

            out <<= 1

            lastbit = (n & 1)

            out ^= lastbit

            n >>= 1

        return out
        """
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        
        return res
        