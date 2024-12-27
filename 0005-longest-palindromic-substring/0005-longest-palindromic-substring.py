class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the palindrome substring

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome (single character center)
            pal1 = expand_around_center(i, i)
            # Even-length palindrome (two character center)
            pal2 = expand_around_center(i, i + 1)
            
            # Update longest palindrome
            if len(pal1) > len(longest):
                longest = pal1
            if len(pal2) > len(longest):
                longest = pal2

        return longest
