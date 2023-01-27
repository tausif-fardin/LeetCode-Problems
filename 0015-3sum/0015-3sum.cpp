class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) break;
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    res.insert({ nums[i], nums[left], nums[right] });
                    left++;
                    right--;
                }
                else if (sum < 0) left++;
                else right--;
            }
        }
        return vector<vector<int>>(res.begin(), res.end());
    }
};