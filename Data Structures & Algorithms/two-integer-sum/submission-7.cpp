class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /*
            TC: O(n)
            SC: O(n)
        */

        unordered_map<int, int> nmap;

        for(int i=0; i<nums.size();i++){
            
            int comp = target - nums[i];

            if (nmap.count(comp)){
                return {nmap[comp], i};
            }
            
            nmap[nums[i]] = i;
        }
        return {-1, -1};
    }
};
