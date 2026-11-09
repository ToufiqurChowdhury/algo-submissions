/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        if (intervals.size() < 1) {
            return 0;
        }

        sort(intervals.begin(), intervals.end(), [](Interval& a, Interval& b) {
            return a.start < b.start;
        });

        priority_queue<int, vector<int>, greater<int>> heap;

        heap.push(intervals[0].end);

        for (int i=1; i<intervals.size(); i++) {

            auto [start, end] = intervals[i];
            if (start >= heap.top()) {
                heap.pop();
            }

            heap.push(end);
        }

        return heap.size();
    }
};
