class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int i=0; i<nums.size(); i++) {
            if (nums[i] > 0) break;
            else if (i>0 && nums[i]==nums[i-1]) continue;
            else twoSum(i, nums, res);
        }

        return res;
    }

private:
    void twoSum(int i, vector<int>& nums, vector<vector<int>>& res) {
        int l = i+1, r = nums.size()-1;

        while (l<r){
            int sum = nums[i] + nums[l] + nums[r];

            if (sum<0) {
                l += 1;
            }
            else if (sum>0) {
                r -= 1;
            }
            else {
                res.push_back({nums[i], nums[l], nums[r]});
                l += 1;

                while (l<r && nums[l]==nums[l-1]){
                    l += 1;
                }
            }
        }
    }
};
