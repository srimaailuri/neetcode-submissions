class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()
        for index, value in enumerate(nums):
            compliment=target-value
            if compliment in seen:
                return [seen[compliment],index]
            seen[value]=index
            

        