class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_list = []
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    new_list.append(i)
                    new_list.append(j)
                    return new_list