from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Stack to store indices of prices
        stack = []
        
        # Traverse the prices list
        for i in range(len(prices)):
            # While the stack is not empty and the current price is less than or equal to the price at the top of the stack
            while stack and prices[i] <= prices[stack[-1]]:
                # Pop the top of the stack and apply the discount
                idx = stack.pop()
                prices[idx] -= prices[i]
            
            # Push the current index onto the stack
            stack.append(i)
        
        return prices
# Instantiate the solution object
solution = Solution()

# Example test case 1
prices = [8, 4, 6, 2, 3]
print(solution.finalPrices(prices))  # Output: [4, 2, 4, 2, 3]

# Example test case 2
prices = [1, 2, 3, 4, 5]
print(solution.finalPrices(prices))  # Output: [1, 2, 3, 4, 5]

# Example test case 3
prices = [10, 1, 1, 6]
print(solution.finalPrices(prices))  # Output: [9, 0, 1, 6]

        