class Solution:
    def numTeams(self, rating):
        n = len(rating)
        result = 0
        
        
        for j in range(1, n - 1):
            left_smaller = 0
            left_larger = 0
            right_smaller = 0
            right_larger = 0
            
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                if rating[i] > rating[j]:
                    left_larger += 1
            
            
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                if rating[k] > rating[j]:
                    right_larger += 1
            
            
            result += left_smaller * right_larger 
            result += left_larger * right_smaller 
        
        return result
 