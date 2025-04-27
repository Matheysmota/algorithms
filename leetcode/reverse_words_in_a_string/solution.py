class Solution:
    def reverseWords(self, s: str):
        res = ''
        left, right = 0, 0
        
        while right < len(s):
            if s[right] != ' ':
                right += 1
            else:
                res += s[left:right+1][::-1]
                right += 1
                left = right
        res += ' '
        res += s[left:right + 2][::-1]
        return res[1:]