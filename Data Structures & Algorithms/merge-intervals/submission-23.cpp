class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // sort intervals
        sort(intervals.begin(), intervals.end(),
            [](const vector<int>& a, const vector<int>& b){
                return a[0] < b[0];
            });
        vector<vector<int>> res;

        res.push_back(intervals[0]);
        for(int i=1; i<intervals.size();i++){
            
            int st = intervals[i][0];
            int et = intervals[i][1];

            int prev_et = res.back()[1];
            if(st <= prev_et){
                res.back()[1] = max(et, prev_et);
            }
            else{
                res.push_back({st,et});
            }
        
        }

        return res;     
    }
};
