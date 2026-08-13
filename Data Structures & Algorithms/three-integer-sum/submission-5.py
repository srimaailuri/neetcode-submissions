class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        sorted_nums=sorted(nums)
        for index, value in enumerate(sorted_nums):
            if index > 0 and sorted_nums[index] == sorted_nums[index - 1]:
                continue
            target=-1*value
            i=index+1;
            length=len(sorted_nums)
            j=length-1
            while i<j and j<length:
                cur_sum=sorted_nums[i]+sorted_nums[j]
                if cur_sum>target:
                    j=j-1
                elif cur_sum<target:
                    i=i+1
                elif cur_sum==target:
                    answer.append([value,sorted_nums[i],sorted_nums[j]])
                    i = i+1
                    j =j- 1
                    while i < j and sorted_nums[i] == sorted_nums[i - 1]:
                        i = i+1
                    while i < j and j+1<length and sorted_nums[j] == sorted_nums[j + 1]:
                        j -= 1
                    
                    
        return answer
                

        