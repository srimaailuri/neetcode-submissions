class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,R=0,0
        length=len(s)
        freq=set()
        max_count=0
        while R<length:
            while s[R] in freq:
                freq.remove(s[L])
                L+=1
            freq.add(s[R])
            R+=1
            max_count=max(max_count,R-L)
        
        return max_count
        