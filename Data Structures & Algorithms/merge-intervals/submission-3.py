class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res = [intervals[0]]

        for startTime, endTime in intervals[1:]:
            prevLastTime = res[-1][1]

            if startTime <= prevLastTime:
                res[-1][1] = max(res[-1][1], endTime)
            else:
                res.append([startTime, endTime])

        return res