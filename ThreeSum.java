import java.util.*;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        
        // Step 1: Sort the array
        Arrays.sort(nums);
        
        // Step 2: Loop through each number in the array
        for (int i = 0; i < nums.length - 2; i++) {
            // Avoid duplicates for the first element
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // Step 3: Use two pointers
            int left = i + 1;
            int right = nums.length - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    // Triplet found
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Move left and right pointers to avoid duplicates
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    // Move to the next unique elements
                    left++;
                    right--;
                } else if (sum < 0) {
                    // If sum is less than 0, move the left pointer to increase the sum
                    left++;
                } else {
                    // If sum is greater than 0, move the right pointer to decrease the sum
                    right--;
                }
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        ThreeSum solution = new ThreeSum();
        int[] nums = {-1, 0, 1, 2, -1, -4};
        
        // Call the threeSum method and print the result
        List<List<Integer>> result = solution.threeSum(nums);
        System.out.println(result);
    }
}