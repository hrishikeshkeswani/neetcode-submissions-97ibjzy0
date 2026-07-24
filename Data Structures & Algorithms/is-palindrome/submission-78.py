class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''
        for char in s:
            if char.isalnum():
                st = st+ char.lower()
        if st == st[::-1]:
            return True
        else:
            return False