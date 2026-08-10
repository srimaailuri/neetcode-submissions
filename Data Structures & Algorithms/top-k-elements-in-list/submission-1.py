class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]

        for num,count in freq.items():
            buckets[count].append(num)

        answer=[]
        for count in range(len(buckets)-1,0,-1):
            for num in buckets[count]:
                answer.append(num)
            
            if len(answer)==k:
                return answer


        

        
        