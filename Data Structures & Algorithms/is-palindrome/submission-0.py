class Solution:
    def isPalindrome(self, s: str) -> bool:
        case_insensitive=s.lower()
        
        i=0
        j=len(case_insensitive)-1

        while i<=j:
            if case_insensitive[i].isalnum()==False:
                i=i+1
            elif case_insensitive[j].isalnum()==False:
                j=j-1
            elif case_insensitive[i]!=case_insensitive[j]:
                return False
            else:
                i=i+1
                j=j-1
        return True