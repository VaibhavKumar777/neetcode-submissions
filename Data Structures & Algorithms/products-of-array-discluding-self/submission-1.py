class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix=[1]*n
        for i in range(n):
            if i!=0:
                prefix[i] = prefix[i-1]*nums[i-1]
            
        suffix = [1]*n
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]
        answer = [1]*n
        for i in range(n):
            answer[i] = prefix[i]*suffix[i]
        return answer
