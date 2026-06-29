class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set <int> seen;
        for(int n : nums){
            if(seen.count(n)){
                return true;
            }else{
                seen.insert(n);
            }
        }
        return false;
    }
};