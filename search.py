#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#You must write an algorithm with O(log n) runtime complexity.


def search(nums, target):
    left, right = 0, len(nums) - 1  # Define the search boundaries
    
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index
        
        if nums[mid] == target:
            return mid  # Target found, return its index
        elif nums[mid] < target:
            left = mid + 1  # Narrow the search to the right half
        else:
            right = mid - 1  # Narrow the search to the left half
    
    return -1  # Target not found