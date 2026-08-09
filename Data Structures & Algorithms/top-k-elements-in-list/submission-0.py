class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_counter=Counter(nums)
        data=my_counter.most_common(k)
        answer=[t[0] for t in data]
        return answer
        