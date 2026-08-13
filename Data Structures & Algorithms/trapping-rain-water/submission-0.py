class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=list()
        prefix.append(0)
        for i in range(len(height)-1):
            prefix.append(max(prefix[i],height[i]))
        suffix=0
        max_capacity=0
        for i in range(len(height)-1,-1,-1):
            max_capacity=max_capacity+max(0,min(suffix,prefix[i])-height[i])
            suffix=max(suffix,height[i])
        return max_capacity
        



        