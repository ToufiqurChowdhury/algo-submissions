class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # TC: nlogn
        
        res = 0
        intervals.sort()

        prev_et = intervals[0][1]

        for st, et in intervals[1:]:

            if st >= prev_et:
                prev_et = et
            else:
                res += 1
                prev_et = min(prev_et, et) # take min because it will not opverlap for the next intervals
        
        return res