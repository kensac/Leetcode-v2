class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(left, right) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return check_palindrome(left + 1, right) or check_palindrome(
                    left, right - 1
                )
            left += 1
            right -= 1
        return True
