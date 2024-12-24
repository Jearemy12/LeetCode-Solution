class Solution:
    def canBeEqual(self, target, arr):
        
        return sorted(target) == sorted(arr)
