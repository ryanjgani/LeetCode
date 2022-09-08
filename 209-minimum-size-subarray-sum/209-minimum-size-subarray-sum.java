class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int res = Integer.MAX_VALUE;
        int l = 0;
        int count = 0;
        for(int r = 0; r < nums.length; r++){
            count += nums[r];
            while(count >= target && l <= r){
                int temp = Math.min(r - l + 1, res);
                res = temp;
                count -= nums[l];
                l += 1;
            }
        }
        if(res < Integer.MAX_VALUE){
            return res;
        }
        return 0;
        
    }
}