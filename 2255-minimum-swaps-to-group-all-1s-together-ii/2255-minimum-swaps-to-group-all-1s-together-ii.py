class Solution:
    def minSwaps(self, nums):
        total_ones = sum(nums)  # Total number of 1's in the array
        n = len(nums)
        
        if total_ones == 0 or total_ones == n:
            return 0  # No swaps needed if all are 0's or all are 1's
        
        # Step 1: Use sliding window to find the max number of 1's in any window of size `total_ones`
        max_ones_in_window = 0
        current_ones = 0
        
        # Initialize the first window
        for i in range(total_ones):
            if nums[i] == 1:
                current_ones += 1
        max_ones_in_window = current_ones
        
        # Slide the window across the array (considering the circular nature)
        for i in range(1, n):
            # Remove the element going out of the window and add the new one coming into the window
            if nums[i - 1] == 1:
                current_ones -= 1
            if nums[(i + total_ones - 1) % n] == 1:
                current_ones += 1
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        # Step 2: The minimum swaps is total_ones - max_ones_in_window
        return total_ones - max_ones_in_window
