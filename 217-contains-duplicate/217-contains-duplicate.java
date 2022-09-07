class Solution {
    public boolean containsDuplicate(int[] nums) {
        final Set<Integer> distinct = new HashSet<Integer>();
        for(int n: nums){
            if(distinct.contains(n)){
                return true;
            }
            distinct.add(n);
        }
        return false;
        
    }
}