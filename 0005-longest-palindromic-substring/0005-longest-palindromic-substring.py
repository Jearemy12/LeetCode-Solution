class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  

        longest = ""
        for i in range(len(s)):
            
            pal1 = expand_around_center(i, i)
           
            pal2 = expand_around_center(i, i + 1)
            
            
            if len(pal1) > len(longest):
                longest = pal1
            if len(pal2) > len(longest):
                longest = pal2

        return longest
