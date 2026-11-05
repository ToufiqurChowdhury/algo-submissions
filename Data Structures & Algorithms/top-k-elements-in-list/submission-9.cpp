class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int, int> count;
        for (int n: nums){
            count[n]++;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        for(auto& entry : count){
            heap.push({entry.second, entry.first}); //cnt, num

            if (heap.size()>k){
                heap.pop();
            }
        }

        vector<int> res;
        while(!heap.empty()){
            res.push_back(heap.top().second);
            heap.pop();
        }
        
        return res;
    }
};
