class Solution {
public:
    int search(vector<int>& nums, int target) {

        int l = 0, r = nums.size()-1;

        while (l<=r){
            int m = (l+r); // 2 
            if (nums[m] == target)
                return m;
            
            //left sorted array
            if (nums[l] <= nums[m])
                if (target > nums[m] or target < nums[l])
                    l = m+1;
                else
                    r = m-1;

            //right sorted array
            else
                if (target < nums[m] or target > nums[r])
                    r = m-1;
                else
                    l = m+1;
        }

        return -1;  
    }
};
