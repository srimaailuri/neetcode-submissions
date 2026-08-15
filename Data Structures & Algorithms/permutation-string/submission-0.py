class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hashmap=Counter(s1)
        length=len(s1)
        s2_hashmap=Counter(s2[:length])
        if s1_hashmap==s2_hashmap:
            return True

        L=0
        R=length
        while R<len(s2):
            s2_hashmap[s2[L]]-=1;
            if s2_hashmap[s2[L]]==0:
                del s2_hashmap[s2[L]]
            s2_hashmap[s2[R]]=s2_hashmap.get(s2[R],0)+1
            if s1_hashmap==s2_hashmap:
                return True
            L+=1
            R+=1
        return False


        