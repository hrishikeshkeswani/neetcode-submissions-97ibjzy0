class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ''
        for char in s:
            if char.isalnum():
                str+= char.lower()
        left = 0
        right = len(str)-1
        while left<right:
            if str[left] == str[right]:
                left+=1
                right -=1
            else:
                return False      
        return True
        
