class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = sorted(set(nums))
        length=len(result)
        max_len=0
        i=0
        j=1
        if length==1:
            return 1
        while j<length and i<length:
            while j<length and i<length and result[j]-result[j-1]==1:
                j=j+1
            cur_len=j-i
            if cur_len>max_len:
                max_len=cur_len
            i=j
            j=j+1
        return max_len