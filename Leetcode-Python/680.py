# 680. Valid Palindrome II
# 難在要用第二個function去判斷刪掉一個字後還會不會一樣

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.validPalindromeUtil(s, left + 1, right) or self.validPalindromeUtil(s, left, right - 1)
        return True

    def validPalindromeUtil(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
