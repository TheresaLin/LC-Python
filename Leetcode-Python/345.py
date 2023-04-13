# 345. Reverse Vowels of a String
# 先把string轉成list，比較好交換字母，再用join轉回string


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = "AEIOUaeiou"
        if not s:
            return
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
        return "".join(s)