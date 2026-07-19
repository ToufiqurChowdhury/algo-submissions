"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # algo: intervals and use free rooms
        # TC: O(nlogn)
        # SC: O(n)
        
        starts = sorted([i.start for i in intervals]) # [1, 5, 15]
        ends = sorted([i.end for i in intervals]) #     [10, 20, 40] cnt = 2

        res, count = 0, 0
        s, e = 0, 0

        for i in range(len(starts)):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res