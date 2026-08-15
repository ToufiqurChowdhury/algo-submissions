class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #intervals.sort(key=lambda x:x[0])
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for st, et in intervals[1:]:
            prev_et = res[-1][1]

            if st <= prev_et:
                res[-1][1] = max(et, prev_et)
            else:
                res.append([st, et])

        return res