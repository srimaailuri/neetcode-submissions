class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        count=1
        longest=0

        seen=set()

        for n in numSet:
            if n not in seen:
                if(n-1) not in numSet:
                    count=1

                    while n+count in numSet:
                        count+=1
                    
                    longest=max(longest,count)
                    count=1

        return longest