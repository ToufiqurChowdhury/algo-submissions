class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /*
            TC: O(n)
            SC: O(n)
        */

        unordered_map<int, int> nmap;

        for (int i; i < nums.size(); i++){

            int need = target - nums[i];
            auto it = nmap.find(need);

            if ( it != nmap.end()){
                return {nmap[need], i};
            }
            
            nmap[nums[i]] = i;
        }

        return {-1, -1};
    }
};
