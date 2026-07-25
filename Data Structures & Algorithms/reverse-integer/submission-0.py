class Solution:
    def reverse(self, x: int) -> int:

        res = 0
        tmp = x

        MAX = 2147483647
        MIN = -2147483648

        while tmp:

            digit = int(math.fmod(tmp, 10))
            tmp = int(tmp/10)

            if(res > MAX/10 or (res == MAX and digit >= MAX % 10)):
                return 0
            if(res < MIN/10 or (res == MIN and digit <= MIN % 10)):
                return 0

            res = (res * 10) + digit

        return res 
        