class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(enumerate(position), key=lambda x: x[1])
        times=[]
        for i in range(len(position)):
            time=int(target-sorted_pairs[i][1])/speed[sorted_pairs[i][0]]
            times.append(time)
        stack=[]
        for i in range(len(times)-1,-1,-1):
            if not stack:
                stack.append(times[i])
            else:
                if stack[-1]<times[i]:
                    stack.append(times[i])
        
        return len(stack)



        