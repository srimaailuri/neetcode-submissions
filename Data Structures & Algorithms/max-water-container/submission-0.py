class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_capacity=0
        while i<j:
            cur_capacity=min(heights[i], heights[j])*(j-i)
            if max_capacity<cur_capacity:
                max_capacity=cur_capacity
            if heights[i]>heights[j]:
                j=j-1
            else:
                i=i+1
        return max_capacity
        