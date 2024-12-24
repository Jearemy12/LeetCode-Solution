class Solution:
    def minSwaps(self, nums):
        total_ones = sum(nums)  
        n = len(nums)
        
        if total_ones == 0 or total_ones == n:
            return 0  
        
        max_ones_in_window = 0
        current_ones = 0
        
        for i in range(total_ones):
            if nums[i] == 1:
                current_ones += 1
        max_ones_in_window = current_ones
        
        for i in range(1, n):
            if nums[i - 1] == 1:
                current_ones -= 1
            if nums[(i + total_ones - 1) % n] == 1:
                current_ones += 1
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        
        return total_ones - max_ones_in_window
