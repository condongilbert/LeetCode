public class removeDuplicates {
    public int removeDup(int[] nums) {
    
    

        int i=0;
      
    
        for (int j=1; j<nums.length; j++){
            if(nums[i]!=nums[j]){
                i++;
                nums[i]=nums[j];
            }
           
        }
        return i+1;
    }
    
}
