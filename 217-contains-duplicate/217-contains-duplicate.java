class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int prev = 0;
        for(int i = 0; i < nums.length; i++){
            if(i > 0 && prev == nums[i]){
                return true;
            }
            prev = nums[i];
        }
        return false;
        
    }
}