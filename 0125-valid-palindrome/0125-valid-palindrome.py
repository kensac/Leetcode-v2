class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean up
        s = s.lower()
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char)

        l = 0
        r = len(chars) - 1

        while l <= r:
            if chars[l] != chars[r]:
                return False
            l += 1
            r -= 1
        return True
