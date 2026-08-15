class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        dq=deque()
        L=0

        for R in range(len(nums)):

            ## Expired value at start of deque(max_element)
            while dq and dq[0]<L:
                dq.popleft()
            
            while dq and nums[dq[-1]]<nums[R]:
                dq.pop()

            dq.append(R)

            if R-L+1==k:
                output.append(nums[dq[0]])
                L+=1
        return output
        