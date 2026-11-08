class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> res(temperatures.size(), 0);
        std::stack<pair<int, int>> tempStk;

        for (int i=0; i<temperatures.size(); i++) {
            while (!tempStk.empty() && tempStk.top().first < temperatures[i]){
                res[tempStk.top().second] = i - tempStk.top().second;
                tempStk.pop();
            }

            tempStk.push({temperatures[i], i});
        }

        return res;
    }
};