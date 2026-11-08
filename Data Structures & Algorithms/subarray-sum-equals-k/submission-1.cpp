class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {

        int res = 0, curSum = 0;

        unordered_map<int, int> prefixSums = {{0,1}};

        for (int num : nums){
            
            curSum += num;
            auto diff = curSum - k;
            if (prefixSums.count(diff)){
                res += prefixSums[diff];
            }
            prefixSums[curSum] ++;
        }

        return res;
        
    }
};