class Solution:
    def mySqrt(self, x: int) -> int:
        if x<0:
            print("Invalid input")
        
        if x == 0:
            return 0

        guess = x/2
        tolerance = 0.00001

        while True:
            newGuess = 0.5 * (guess + x/guess)

            if abs(newGuess - guess) < tolerance:
                return int(newGuess)
            
            guess = newGuess      