class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        // 1. Count frequency
        unordered_map<int, int> count;
        for (int n: nums){
            count[n]++;
        }

        // 2. Min-heap: {frequency, number}
        priority_queue<
            pair<int, int>, 
            vector<pair<int, int>>, 
            greater<pair<int, int>>> heap;

        // 3. Keep only top K frequent elements
        for(auto& item : count){
            int num = item.first;
            int freq = item.second;

            heap.push({freq, num}); //cnt, num

            if (heap.size()>k){
                heap.pop();
            }
        }

        // 4. Extract results
        vector<int> res;
        while(!heap.empty()){
            int num = heap.top().second;
            res.push_back(num);
            heap.pop();
        }
        
        return res;
    }
};
