class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prev_et = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_et:
                prev_et = end
            else:
                res += 1
                prev_et = min(prev_et, end)

        return res