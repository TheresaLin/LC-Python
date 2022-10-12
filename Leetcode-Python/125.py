## Valid Palindrome：除去大小寫和奇怪的標點符號，是回文串的return True
## 相向雙指針：two pointers


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 設定two pointers
        left, right = 0, len(s) - 1
        while left < right:
            # 注意第二層while還是要檢查 left < right
            # 開始檢查是不是數字或字符，不是的就跳下一位
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1
            # 發現left != right return False
            if left < right and s[left].lower() != s[right].lower():
                return False

            # 都相等，指針繼續走
            left += 1
            right -= 1
        # 全部檢查完return True
        return True
            
    # 自定一個function，檢查是不是數字或字符        
    def is_valid(self, char):
        return char.isdigit() or char.isalpha()