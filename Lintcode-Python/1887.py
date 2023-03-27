## 1887. Stretch Word
# Solution: iterate the string and use counter to count the number of the same character occurrences,
# If a character appears more than twice, then the answer would be multiplied by 2


# 1st point: answer should be at least 1 
#            because this string would contain at least one character
# 2nd point: If there's a repeat character, 
#            then the answer should be multiply by 2
# 3rd point: counter is counting for the number of the same character occurrences


class Solution:
    """
    @param s: the string
    @return: The numbers of strings
    """
    def stretch_word(self, s: str) -> int:
        answer = 1
        index = 0
        while index + 1 < len(s):
            counter = 1
            while index + 1 < len(s) and s[index] == s[index + 1]:
                index += 1
                counter += 1
            if counter >= 2:
                answer = answer * 2
            index += 1
        return answer

            

