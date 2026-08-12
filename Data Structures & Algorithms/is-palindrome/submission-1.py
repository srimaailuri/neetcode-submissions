class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i=0
        j=len(s)-1

        while i<=j:
            if s[i].isalnum()==False:
                i=i+1
            elif s[j].isalnum()==False:
                j=j-1
            elif s[i].lower()!=s[j].lower():
                return False
            else:
                i=i+1
                j=j-1
        return True