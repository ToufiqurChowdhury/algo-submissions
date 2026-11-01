class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        stack = [] # stack the duration to reach dest

        for p, s in sorted(pair)[::-1]: # sorted reverse pairs
            stack.append((target-p)/s) # decimal div
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
