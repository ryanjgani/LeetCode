class Solution {
    public boolean isPalindrome(String s) {
        if(s.isEmpty()){
            return true;
        }
        int l = 0;
        int r = s.length() - 1;
        char i, j;
        while(l <= r){
            i = s.charAt(l);
            j = s.charAt(r);
            
            if (!Character.isLetterOrDigit(i)){
                l += 1;
            }
            else if (!Character.isLetterOrDigit(j)){
                r -= 1;
            }
            else if(Character.toLowerCase(i) != Character.toLowerCase(j)){
                return false;
            }
            else {
                
            r -= 1;
            l += 1;
            }

        }
        return true;
        
        
        
        
        
    }
}