class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L,R=0,0
        length=len(s)
        freq={}
        max_count=0
        max_freq = 0
        while R <length:
            freq[s[R]]=freq.get(s[R],0)+1
            max_freq=max(max_freq,freq[s[R]])
            while (R-L+1)-max_freq>k:
                freq[s[L]]=freq.get(s[L],0)-1
                if freq[s[L]]==0:
                    del freq[s[L]]
                L+=1
                print("L:",L)
            R+=1
            max_count=max(max_count,R-L)

        return max_count

        