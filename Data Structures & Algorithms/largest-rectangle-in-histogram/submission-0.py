class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_capacity=0
        heights.append(0)
        for index, value in enumerate(heights):
            while stack and heights[stack[-1]] > value:
                popped_index = stack.pop()
                height = heights[popped_index]
                width = index if not stack else index - stack[-1] - 1
                max_capacity = max(max_capacity, height * width)
            stack.append(index)
        heights.pop()
        return max_capacity
