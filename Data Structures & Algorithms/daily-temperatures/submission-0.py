class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for index,value in enumerate(temperatures):
            while stack and stack[-1][1]<value:
                b=stack.pop()
                result[b[0]]=index-b[0]
            stack.append((index,value))
        return result


        